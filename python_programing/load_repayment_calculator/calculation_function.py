from input_functions import get_annual_interest_rate, get_loan_amount, get_loan_term

def calculate_repayment():
    loan_amount = get_loan_amount()
    loan_term_in_months = get_loan_term() * 12
    monthly_interest_rate = get_annual_interest_rate() / 100 / 12 

    numerator = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_in_months
    denominator = (1 + monthly_interest_rate) ** loan_term_in_months - 1

    monthly_payment = numerator / denominator
    total_payment = monthly_payment * loan_term_in_months
    
    return monthly_payment, total_payment

