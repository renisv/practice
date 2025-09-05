def get_loan_amount():
    while True:
        try:
            principal = int(input("Enter loan amount: "))
            if principal > 0:
                return principal
            else:
                print("Loan amount must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_annual_interest_rate():
    while True:
        try:
            rate = float(input("Enter interest rate: "))
            if rate >= 0:
                return rate
            else:
                print("Please enter a valid interest rate!")
        except ValueError:
            print("Please enter a valid interest rate!")

def get_loan_term():
    while True:
        try:
            term = int(input("Enter loan term in years: "))
            if term <= 0:
                print("Loan term must be greater than 0.")
            else:
                return term
        except ValueError:
            print("Please enter a valid loan term!")