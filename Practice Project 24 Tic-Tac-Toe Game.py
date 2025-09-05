"""
24.	Tic-Tac-Toe Game
o	Play between two players.
o	Bonus: Add simple AI using random moves.
"""

import random

# Tic-Tac-Toe board
board = [" " for _ in range(9)]  # 0-8 positions

def print_board():
    """Display the current board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(player):
    """Check if the given player has won"""
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_draw():
    """Check if the game is a draw"""
    return " " not in board

def player_move(player):
    """Handle human player move"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move! Position already taken or out of range.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def ai_move(player):
    """Simple AI that picks a random empty spot"""
    empty_positions = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(empty_positions)
    print(f"AI ({player}) chooses position {move + 1}")
    board[move] = player

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Choose mode: 1 = 2 Players, 2 = Play vs AI: ")

    if mode not in ["1", "2"]:
        print("Invalid choice, defaulting to 2 players.")
        mode = "1"

    current_player = "X"
    print_board()

    while True:
        if mode == "2" and current_player == "O":
            ai_move("O")
        else:
            player_move(current_player)

        print_board()

        if check_winner(current_player):
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()


