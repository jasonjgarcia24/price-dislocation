# Import pathlib
from pathlib import Path
from qualifier.filters.loan_to_value import filter_loan_to_value

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters.credit_score   import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value  import filter_loan_to_value
from qualifier.filters.max_loan_size  import filter_max_loan_size

# @TODO: Your code here!
# Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path(r'../data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt                 = 1500
    income               = 4000
    loan                 = 210000
    home_value           = 250000

    dti_ratio = calculators.calculate_monthly_debt_ratio(debt, income)
    ltv_ratio = calculators.calculate_loan_to_value_ratio(loan, home_value)


    def test_filter_credit_score():
        # credit_score >= bank_data[4]
        test_bank_data = [[0, 0, 0, 0, current_credit_score]]
        assert filter_credit_score(current_credit_score, test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, 0, 0, current_credit_score+1]]
        assert filter_credit_score(current_credit_score+1, test_bank_data) == test_bank_data


    def test_debt_to_income():
        # monthly_debt_ratio <= bank_data[3]
        test_bank_data = [[0, 0, 0, dti_ratio]]
        assert filter_debt_to_income(dti_ratio, test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, 0, dti_ratio-1]]
        assert filter_debt_to_income(dti_ratio-1, test_bank_data) == test_bank_data


    def test_loan_to_value():
        # loan_to_value_ratio <= bank_data[2]
        test_bank_data = [[0, 0, ltv_ratio]]
        assert filter_loan_to_value(ltv_ratio, test_bank_data) == test_bank_data

        test_bank_data = [[0, 0, ltv_ratio-1]]
        assert filter_loan_to_value(ltv_ratio-1, test_bank_data) == test_bank_data

    
    def test_max_loan_size():
        # loan_amount <= bank_data[1]
        test_bank_data = [[0, loan]]
        assert filter_max_loan_size(loan, test_bank_data) == test_bank_data

        test_bank_data = [[0, loan-1]]
        assert filter_max_loan_size(loan-1, test_bank_data) == test_bank_data


    test_filter_credit_score()
    test_debt_to_income()
    test_loan_to_value()
    test_max_loan_size()


    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
    def test_save_csv():    
        csvpath = Path(r".\data\output\qualifying_loans.csv")
        assert fileio.save_csv(csvpath, bank_data) == True

