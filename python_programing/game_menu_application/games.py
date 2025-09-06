import random, operator

def guess_the_number():
    random_number = random.randint(1, 100)
    number_of_guesses = 0
    print('Welcome to "Guess the Number" game! You have 7 attempts.')
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            number_of_guesses += 1
                
            if guess > random_number:
                if number_of_guesses == 7:
                    print("Your guess is too high!")
                    print(f"You've used too many tries, you've lost this game! The number was {random_number}.")
                    break
                else:
                    print("Your guess is too high. Try lower!")
            elif guess < random_number:
                if number_of_guesses == 7:
                    print("Your guess is too low!")
                    print(f"You've used too many tries, you've lost this game! The number was {random_number}.")
                    break
                else:
                    print("Your guess is too low. Try higher!")
            else:
                print("Congratulations! You guessed the right number.")
                break
            
            print(f"You have used {number_of_guesses} attempts so far.\n")
            
        except ValueError:
            print("Please enter a number from 1 to 100!")
    
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        print("\n" + "="*50 + "\n")
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye!")



def rock_paper_scissors():
    moves = {1: "Rock", 2: "Paper", 3: "Scissors"}
    results = {
        (1, 3): "player",    # Rock beats Scissors
        (2, 1): "player",    # Paper beats Rock
        (3, 2): "player",    # Scissors beats Paper
        (1, 2): "computer",  # Rock loses to Paper
        (2, 3): "computer",  # Paper loses to Scissors
        (3, 1): "computer",  # Scissors loses to Rock
    }
    
    print("Welcome to Rock Paper Scissors!")
    print("1: Rock, 2: Paper, 3: Scissors")
    
    try:
        player_choice = int(input("Enter your choice (1-3): "))
        if player_choice not in [1, 2, 3]:
            print("Please enter 1, 2, or 3!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return
    
    computer_choice = random.randint(1, 3)
    
    print(f"\nYou chose: {moves[player_choice]}")
    print(f"Computer chose: {moves[computer_choice]}")
    
    if player_choice == computer_choice:
        print("It's a draw!")
    else:
        winner = results[(player_choice, computer_choice)]
        if winner == "player":
            print("You win! 🎉")
        else:
            print("Computer wins! 🤖")

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        print("\n" + "="*30)
        rock_paper_scissors()
    else:
        print("Thanks for playing!")



def math_quiz():
    score = 0
    total_questions = 5
    
    print(f"Math Quiz! You'll get {total_questions} questions.\n")
    
    for question_num in range(1, total_questions + 1):
        print(f"Question {question_num}:")
        
        op_symbol, op_func = random.choice([
            ('+', operator.add),
            ('-', operator.sub),
            ('*', operator.mul),
            ('/', operator.truediv)
        ])
        
        a, b = random.randint(1, 10), random.randint(1, 10)
        
        print(f"{a} {op_symbol} {b} = ?")
        
        try:
            answer = float(input("Enter your answer: "))
            correct = op_func(a, b)
            
            if abs(answer - correct) < 0.001:
                print("Correct! ✅")
                score += 1
            else:
                print(f"Wrong! ❌ Correct answer: {correct:.2f}")
                
        except ValueError:
            print("Please enter a valid number! ❌")
        
        print()  
    
    print("="*40)
    print(f"Quiz completed! Your score: {score}/{total_questions}")
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        print("\n" + "="*30)
        math_quiz()
    else:
        print("Thanks for playing!")
