"""
10.	Simple Hangman Game
o	User guesses letters of a word.
o	Show remaining attempts.
"""
import random

def hangman():
    words = ["python", "hangman", "challenge", "programming"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

        # Show current state of the word
        current_state = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(current_state)

        if "_" not in current_state:
            print("Congratulations! You've guessed the word.")
            break
    else:
        print(f"Game over! The word was: {word}")

# Run the Hangman game
hangman()