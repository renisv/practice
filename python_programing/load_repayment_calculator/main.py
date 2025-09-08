#!/usr/bin/env python3

from calculation_function import calculate_repayment

def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("        LOAN REPAYMENT CALCULATOR")
    print("=" * 50)
    print("This program helps you calculate:")
    print("• Your monthly loan payment")
    print("• Total amount you'll pay over the loan term")
    print()

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

def main():
    display_welcome()
    
    try:
        monthly, total = calculate_repayment()
        
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

if __name__ == "__main__":
    while True:
        main()
        if not ask_to_continue():
            print("\nThank you for using the Loan Repayment Calculator!")
            print("Goodbye!")
            break