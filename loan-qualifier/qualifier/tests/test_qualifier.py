import os

# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters.credit_score   import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value  import filter_loan_to_value
from qualifier.filters.max_loan_size  import filter_max_loan_size

test_path = os.path.dirname(os.path.realpath(__file__))
prnt_path = os.path.dirname(test_path)

# @TODO: Your code here!
# Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) != 0.370

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) != 0.80

def test_filters():
    bank_data = fileio.load_csv(Path(f"{prnt_path}\\data\\daily_rate_sheet.csv"))
    current_credit_score = 750
    debt                 = 1500
    income               = 4000
    loan                 = 210000
    home_value           = 250000

    dti_ratio = calculators.calculate_monthly_debt_ratio(debt, income)
    ltv_ratio = calculators.calculate_loan_to_value_ratio(loan, home_value)


    def test_filter_credit_score():
        # credit_score >= bank_data[4]
        test_bank_data = [[0, 0, 0, 0, current_credit_score]]       # Tests for ==      --TRUE case
        assert filter_credit_score(current_credit_score,   test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, 0, 0, current_credit_score+1]]     # Tests for >      --TRUE case
        assert filter_credit_score(current_credit_score+1, test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, 0, 0, current_credit_score+1]]     # Tests for <      --FALSE case
        assert filter_credit_score(current_credit_score, test_bank_data) != test_bank_data


    def test_debt_to_income():
        # monthly_debt_ratio <= bank_data[3]
        test_bank_data = [[0, 0, 0, dti_ratio]]     # Tests for ==      --TRUE case
        assert filter_debt_to_income(dti_ratio,   test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, 0, dti_ratio-1]]   # Tests for <       --TRUE case
        assert filter_debt_to_income(dti_ratio-1, test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, 0, dti_ratio-1]]   # Tests for >       --FALSE case
        assert filter_debt_to_income(dti_ratio, test_bank_data) != test_bank_data


    def test_loan_to_value():
        # loan_to_value_ratio <= bank_data[2]
        test_bank_data = [[0, 0, ltv_ratio]]        # Tests for ==      --TRUE case
        assert filter_loan_to_value(ltv_ratio,   test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, ltv_ratio-1]]      # Tests for <      --TRUE case
        assert filter_loan_to_value(ltv_ratio-1, test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, ltv_ratio-1]]      # Tests for >      --FALSE case
        assert filter_loan_to_value(ltv_ratio, test_bank_data) != test_bank_data

    
    def test_max_loan_size():
        # loan_amount <= bank_data[1]
        test_bank_data = [[0, loan]]        # Tests for ==      --TRUE case
        assert filter_max_loan_size(loan,   test_bank_data) == test_bank_data

        test_bank_data = [[0, loan-1]]      # Tests for <      --TRUE case
        assert filter_max_loan_size(loan-1, test_bank_data) == test_bank_data

        test_bank_data = [[0, loan-1]]      # Tests for >      --FALSE case
        assert filter_max_loan_size(loan, test_bank_data) != test_bank_data


    test_filter_credit_score()
    test_debt_to_income()
    test_loan_to_value()
    test_max_loan_size()


    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
def test_fileio():
    def test_save_csv():
        csvpath = Path(f"{test_path}\\data\\qualifying_loans.csv")
        bank_data = [
                ['r1c1','r1c2','r1c3','r1c4','r1c5','r1c6'],
                ['r2c1','r2c2','r2c3','r2c4','r2c5',],
                ['r3c1','r3c2',None,'r3c4',None,],
                [None]
            ]
        assert fileio.save_csv(csvpath, bank_data) == True
        os.remove(csvpath)

    test_save_csv()

