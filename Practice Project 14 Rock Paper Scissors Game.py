"""
14.	Rock-Paper-Scissors Game
o	Play against the computer with input validation.
"""

import random  # to let the computer choose randomly

def rock_paper_scissors():
    choices = ["Rock", "Paper", "Scissor"]
    print("Welcome to the Rock, Scissors, Paper Game!")
    
    while True:
        user_input = input("Enter a word from Rock, Scissor, or Paper, or type Exit to quit the game: ").lower()
                             
        if user_input == "exit":
            print("Thank you for playing the game!\n")
            break
        elif user_input not in [choice.lower() for choice in choices]:
            print("Invalid input! Please try again.\n")
            continue

        comp_selection = random.choice(choices).lower()
        print("Computer selection is", comp_selection.title())

        if user_input == comp_selection:
            print("Its a tie!\n")
            continue
        elif (
            (user_input == "rock" and comp_selection=="scissor") or
            (user_input == "scissor" and comp_selection=="paper") or
            (user_input == "paper" and comp_selection=="rock")):
                print("User wins!\n")

        else:
            print("Computer wins!\n")

#Run the function
rock_paper_scissors()
