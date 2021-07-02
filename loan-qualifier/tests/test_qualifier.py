# -*- coding: utf-8 -*-
"""PyTest Test Suite for LOAN-QUALIFIER Package.

This module allows you to use the standard python assert for verifying expectations and values
within the loan-qualifier app.

Example:
    $ pytest tests

    OR

    $ pytest
"""
import os

# Import pathlib
from pathlib import Path

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters.credit_score   import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value  import filter_loan_to_value
from qualifier.filters.max_loan_size  import filter_max_loan_size

#Import fileio
from qualifier.utils import fileio

# Import Validators
from qualifier.utils import validators

test_path = os.path.dirname(os.path.realpath(__file__))
prnt_path = os.path.dirname(test_path)


def test_filters():
    ''' PyTest function for testing all modules' functions in the qualifier.filters
        internal library.

        TESTED FUNCTIONS:
            - credit_score.filter_credit_score()
            - debt_to_income.filter_debt_to_income()
            - loan_to_value.filter_loan_to_value()
            - max_loan_size.filter_max_loan_size()
    '''
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
        test_bank_data = [[0, 0, 0, 0, current_credit_score],       # Tests for ==  --TRUE case
                          [0, 0, 0, 0, current_credit_score-1],     # Tests for >   --TRUE case
                          [0, 0, 0, 0, current_credit_score+1]]     # Tests for <   --FALSE case
        assert filter_credit_score(current_credit_score, test_bank_data) == test_bank_data[0:2]


    def test_debt_to_income():
        # monthly_debt_ratio <= bank_data[3]
        test_bank_data = [[0, 0, 0, dti_ratio],                     # Tests for ==  --TRUE case
                          [0, 0, 0, dti_ratio+0.1],                 # Tests for <   --TRUE case
                          [0, 0, 0, dti_ratio-0.1]]                 # Tests for >   --FALSE case
        assert filter_debt_to_income(dti_ratio, test_bank_data) == test_bank_data[0:2]


    def test_loan_to_value():
        # loan_to_value_ratio <= bank_data[2]
        test_bank_data = [[0, 0, ltv_ratio],                        # Tests for ==  --TRUE case
                          [0, 0, ltv_ratio+0.1],                    # Tests for <   --TRUE case
                          [0, 0, ltv_ratio-0.1]]                    # Tests for >   --FALSE case
        assert filter_loan_to_value(ltv_ratio, test_bank_data) == test_bank_data[0:2]

    
    def test_max_loan_size():
        # loan_amount <= bank_data[1]
        test_bank_data = [[0, loan],                                # Tests for ==  --TRUE case
                          [0, loan+1],                              # Tests for <   --TRUE case
                          [0, loan-1]]                              # Tests for >   --FALSE case
        assert filter_max_loan_size(loan, test_bank_data) == test_bank_data[0:2]


    test_filter_credit_score()
    test_debt_to_income()
    test_loan_to_value()
    test_max_loan_size()


def test_calculators():
    ''' PyTest function for testing all functions in the qualifier.utils.calculators
        module.

        TESTED FUNCTIONS:
            - calculators.calculate_monthly_debt_ratio()
            - calculators.calculate_loan_to_value_ratio()
    '''
    def test_calculate_monthly_debt_ratio():
        assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375
        assert calculators.calculate_monthly_debt_ratio(1500, 4000) != 0.370

    def test_calculate_loan_to_value_ratio():
        assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84
        assert calculators.calculate_loan_to_value_ratio(210000, 250000) != 0.80

    test_calculate_monthly_debt_ratio()
    test_calculate_loan_to_value_ratio()


def test_fileio():
    ''' PyTest function for testing all functions in the qualifier.utils.fileio
        internal module.

        TESTED FUNCTIONS:
            - fileio.load_csv()
            - fileio.save_csv()
    '''
    csvpath_read  = Path(f"{test_path}\\data\\input\\test_data.csv")
    csvpath_write = Path(f"{test_path}\\data\\output\\test_data.csv")

    test_data = [
            ['hdr1','hdr2','hdr3','hdr4','hdr5'],
            ['r1c1','r1c2','r1c3','r1c4','r1c5','r1c6'],
            ['r2c1','r2c2','r2c3','r2c4','r2c5',],
            ['r3c1','r3c2','','r3c4','',],
            ['']
        ]
    
    def test_load_csv():
        # Since fileio.load_csv() does not return header,
        # compare with test_data[1:].
        assert fileio.load_csv(csvpath_read) == test_data[1:]

    def test_save_csv():
        assert fileio.save_csv(csvpath_write, test_data) == True

    test_load_csv()
    test_save_csv()


def test_validators():
    ''' PyTest function for testing all functions in the qualifier.utils.validators
        module.

        TESTED FUNCTIONS:
            - validators.test_csv_ext_validator()
            - validators.test_csv_exist_validator()
            - validators.csv_no_overwrite_validator()
            - validators.prnt_path_validator()
    '''
    def test_csv_ext_validator():
        assert validators.csv_ext_validator(f"{test_path}\\data\\input\\test_data.csv") == True
        assert validators.csv_ext_validator(f"{test_path}\\data\\input\\test_data.bad") != True

    def test_csv_exist_validator():
        # IMPORTANT: Do not delete f"{test_path}\\data\\input\\test_data.csv". If it is removed,
        # this test will FAIL.
        assert validators.csv_exist_validator(f"{test_path}\\data\\input\\test_data.csv") == True
        assert validators.csv_exist_validator(f"{test_path}\\data\\input\\test_data.bad") != True
        assert validators.csv_exist_validator(f"{test_path}\\data\\input\\no_file.csv")   != True

    def test_csv_no_overwrite_validator():
        # IMPORTANT: Do not delete f"{test_path}\\data\\input\\test_data.csv". If it is removed,
        # this test will FAIL.
        assert validators.csv_no_overwrite_validator(f"{test_path}\\data\\input\\test_data.csv") != True
        assert validators.csv_no_overwrite_validator(f"{test_path}\\data\\input\\no_file.csv")   == True

    def test_path_validator():
        assert validators.prnt_path_validator(f"{test_path}\\data\\input\\")      == True
        assert validators.prnt_path_validator(f"{test_path}\\data\\not_a_path\\") != True

    test_csv_ext_validator()
    test_csv_exist_validator()
    test_csv_no_overwrite_validator()
    test_path_validator()