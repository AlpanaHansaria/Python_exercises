"""
2.	Number Guessing Game
o	Program chooses a random number (1–100). User guesses until correct.
o	Give hints: “Too high” or “Too low.”
"""
import random       

def is_valid_number(expr):
    """Check if the expression contains only numbers."""
    for num in expr:
        if not num.isdigit():
            return False
    return True

def guessing_game():
    print("Welcome to the Guessing Game!")
    
    while True:  # Loop to allow replaying the game
        secret_number = random.randint(1, 100)
        attempts = 0

        while True:
            expr = input("Guess the number: ")
            if expr.lower() == 'exit':
                print("Exiting game. Goodbye!")
                return  # Exit the game completely
            
            # Check if input is a valid number
            if not is_valid_number(expr):
                print("Invalid input! Only numbers are allowed.")
                continue
            
            try:
                guess = int(expr)
                attempts += 1

                if guess < secret_number:
                    print("Too low!")
                elif guess > secret_number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        # Ask user if they want to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Run the guessing game
guessing_game()
