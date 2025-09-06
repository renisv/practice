from games import guess_the_number, rock_paper_scissors, math_quiz

def main_menu():
    while True:
        print("\n" + "="*40)
        print("🎮 GAME COLLECTION - MAIN MENU")
        print("="*40)
        print("1. Guess the Number")
        print("2. Rock Paper Scissors")
        print("3. Math Quiz")
        print("4. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            guess_the_number()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            math_quiz()
        elif choice == '4':
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()