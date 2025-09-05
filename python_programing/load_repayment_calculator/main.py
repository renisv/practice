#!/usr/bin/env python3
"""
Loan Repayment Calculator
A simple program to calculate monthly loan payments and total repayment amount.
"""

from calculation_function import calculate_repayment

def display_welcome():
    """Display welcome message and program information"""
    print("=" * 50)
    print("        LOAN REPAYMENT CALCULATOR")
    print("=" * 50)
    print("This program helps you calculate:")
    print("• Your monthly loan payment")
    print("• Total amount you'll pay over the loan term")
    print("• Total interest you'll pay")
    print()

def display_results(monthly_payment, total_payment, loan_amount):
    """Display the calculation results in a formatted way"""
    interest_paid = total_payment - loan_amount
    
    print("\n" + "=" * 50)
    print("           CALCULATION RESULTS")
    print("=" * 50)
    print(f"Monthly Payment:       ${monthly_payment:>10.2f}")
    print(f"Total Amount Paid:     ${total_payment:>10.2f}")
    print(f"Principal Amount:      ${loan_amount:>10.2f}")
    print(f"Total Interest Paid:   ${interest_paid:>10.2f}")
    print("=" * 50)

def main():
    """Main program function"""
    display_welcome()
    
    try:
        # Get the loan details from user and calculate
        monthly, total = calculate_repayment()
        
        # Since we can't directly get the loan amount from calculate_repayment,
        # we'll need to modify our approach or adjust the display
        # For now, we'll just show the monthly and total
        print("\n" + "=" * 50)
        print("           CALCULATION RESULTS")
        print("=" * 50)
        print(f"Monthly Payment:     ${monthly:>10.2f}")
        print(f"Total Amount Paid:   ${total:>10.2f}")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def ask_to_continue():
    """Ask user if they want to perform another calculation"""
    while True:
        response = input("\nWould you like to calculate another loan? (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    while True:
        main()
        if not ask_to_continue():
            print("\nThank you for using the Loan Repayment Calculator!")
            print("Goodbye!")
            break