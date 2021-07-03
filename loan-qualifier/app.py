# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import os
import sys
import fire
import questionary

from io      import FileIO
from pathlib import Path

from qualifier.utils.fileio           import load_csv, save_csv
from qualifier.filters.max_loan_size  import filter_max_loan_size
from qualifier.filters.credit_score   import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value  import filter_loan_to_value

from qualifier.utils.validators import (
    csv_ext_validator,
    csv_exist_validator,
    csv_no_overwrite_validator
)
from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio
)

app_path  = os.path.dirname(os.path.realpath(__file__))
prnt_path = os.path.dirname(app_path)
full_path  = lambda file_path: f"{prnt_path}\\{file_path}".replace(prnt_path, ".")

no_action_str          = "Ok! No action has been taken."
no_income_str          = "Sorry! You need a monthly income for qualifying loans."
no_qualifying_loan_str = "Sorry! You do not have any qualifying loans."
no_save_str            = "Ok! Your data was not saved."


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Args:
        No args.

    Returns:
        csvdata (list): A list of lists that contains the rows of bank data from
        the CSV file. Or, an empty list if the user aborts.
    """
    # Query the user's file save preferences via CLI:
    choices   = [full_path("data\\daily_rate_sheet.csv"), 'let me tell you']
    questions = [
        {
            "type":        "rawselect",
            "name":        "read_where",
            "message":     "Where do you want to pull your rate-sheet (.csv)?",
            "choices":     choices,
            "instruction": "(select '1' for default)",
        },
        {
            "type":     "path",
            # Intentionally overwrites result from previous question.
            "name":     "read_where",
            "message":  "Enter a file path to a rate-sheet (.csv):",
            "when"   :  lambda x: True if x["read_where"] == choices[-1] else False,
            "validate": csv_exist_validator,
        }
    ]

    csvquery = questionary.prompt(questions)

    # If the user chooses to not continue, exit:
    if not csvquery: return None

    # If the user chooses to continue, perform the following:
    csvpath = Path(csvquery['read_where'])        
    csvdata = load_csv(csvpath)
    
    return csvdata


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Args:
        No args.
    
    Returns:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.
    """

    questions = [
        {
            "type":    "text",
            "name":    "credit_score",
            "message": "What's your credit score?",
            "validate": lambda x: True if x.isnumeric() and 0 <= int(x) <= 850 else "Please enter a positive number between 0 and 850.",
            "filter":   lambda x: int(x),
        },
        {
            "type":    "text",
            "name":    "debt",
            "message": "What's your current amount of monthly debt?",
            "validate": lambda x: True if x.isnumeric() else "Please enter a positive number.",
            "filter":   lambda x: float(x),
        },
        {
            "type":    "text",
            "name":    "income",
            "message": "What's your total monthly income?",
            "validate": lambda x: True if x.isnumeric() else "Please enter a positive number.",
            "filter":   lambda x: float(x),
        },
        {
            "type":    "text",
            "name":    "loan_amount",
            "message": "What's your desired loan amount?",
            "validate": lambda x: True if x.isnumeric() and int(x) != 0 else "Please enter a positive non-zero number.",
            "filter":   lambda x: float(x),
        },
        {
            "type":    "text",
            "name":    "home_value",
            "message": "What's your home value?",
            "validate": lambda x: True if x.isnumeric() else "Please enter a positive number.",
            "filter":   lambda x: float(x),
        },
    ]

    requestor_details = questionary.prompt(questions)

    # If the user chooses to not continue, exit:
    if not requestor_details:
        return [None] * 5

    credit_score, debt, income, loan_amount, home_value = requestor_details.values()
    # credit_score, debt, income, loan_amount, home_value = [850, 1000, 10000, 10000, 100000]

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - credit score
        - loan size
        - debit to income ratio (calculated)
        - loan to value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        bank_data_filtered (list): A list of the banks willing to underwrite the
        loan.
    """
    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):
    """If requested, saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.

    Returns:
        No returns.
    """
    # Query the user's file save preferences via CLI:
    choices   = [full_path("data\\output.csv"), 'let me tell you']
    questions_round1 = [
        {
            "type":    "confirm",
            "name":    "save_question",
            "message": "Would you like to save your qualifying loans?",
        },
        {
            "type":        "rawselect",
            "name":        "save_where",
            "message":     "Where do you want to save your qualifying bank loans (.csv)?",
            "choices":     choices,
            "instruction": "(select '1' for default)",
            "when":        lambda x: x["save_question"],
        },
        {
            "type":     "path",
            # Intentionally overwrites result from previous question.
            "name":     "save_where",
            "message":  "Where do you want to save your qualifying bank loans (.csv)?",
            "when"   :  lambda x: True if x["save_question"] and x["save_where"] == choices[-1] else False,
            "validate": csv_ext_validator,
        },
        {
            "type":    "confirm",
            "name":    "are_you_sure",
            "message": "This file already exists. Do you want to overwrite it?",
            "when"   : lambda x: True if x["save_question"] and Path(x["save_where"]).exists() else False,
        },
    ]

    questions_round2 = [
        {
            "type":     "path",
            "name":     "save_where",
            "message":  "Where do you want to save your qualifying bank loans (.csv)? (Enter a unique filename)",
            "validate": csv_no_overwrite_validator,
        },
    ]

    csvquery = questionary.prompt(questions_round1)

    # If the user chooses to not continue, exit:
    if not csvquery or not csvquery["save_question"]:
        return False

    # If we made it here, the filename was unique and this was never asked:
    if not "are_you_sure" in csvquery:
        csvquery["are_you_sure"] = True

    # If the user chooses to not override an existing file, they will be prompt to 
    # input a unique file:
    if not csvquery["are_you_sure"] :
        csvquery = questionary.prompt(questions_round2)

    # If the user chooses to not continue, exit: 
    if not csvquery:
        return False

    # If the user chooses to save, perform the following:
    csvpath = csvquery["save_where"]
    save_csv(csvpath, qualifying_loans)
    
    return True
    

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()
    if not bank_data:        
        print(no_action_str)
        return

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()    
    if not any([credit_score, debt, income, loan_amount, home_value]):
        print(no_action_str)
        return
    
    # Prompt the user that there are no qualifying loans and exit the program.
    if not income:
        print(no_income_str)
        return

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Prompt the user that there are no qualifying loans and exit the program.
    if not qualifying_loans:
        print(no_qualifying_loan_str)
        return

    # Save qualifying loans
    save_status = save_qualifying_loans(qualifying_loans)
    if not save_status:
        print(no_save_str)
        return


if __name__ == "__main__":
    fire.Fire(run)
