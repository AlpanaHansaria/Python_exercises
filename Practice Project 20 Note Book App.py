"""
20.	Simple Note App
o	Add, view, and delete notes saved in a text file.
"""

import os

# File to store notes
FILE_NAME = "C:\\Users\\Alpan\\OneDrive\\Documents\\GitHub\\Python_exercises\\notes.txt"

# Check if file exists; if not, create it
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass  # just create an empty file

# Load notes from file
with open(FILE_NAME, "r") as f:
    notes = [line.strip() for line in f.readlines()]

def save_notes():
    """Save the current notes to a file"""
    with open(FILE_NAME, "w") as f:
        for note in notes:
            f.write(note + "\n")

def show_menu():
    print("\n--- NOTE-BOOK APP ---")
    print("1. View notes")
    print("2. Add note")
    print("3. Remove note")
    print("4. Exit")

def view_notes():
    if not notes:
        print("No notes yet.")
    else:
        print("\nYour Notes:")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note}")

def add_note():
    note = input("Enter the note: ")
    notes.append(note)
    save_notes()  # Save after adding
    print(f"'{note}' added to the list!")

def remove_note():
    view_notes()
    try:
        note_num = int(input("Enter the number of the note to remove: "))
        if 1 <= note_num <= len(notes):
            removed = notes.pop(note_num - 1)
            save_notes()  # Save after removing
            print(f"Removed: {removed}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        remove_note()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1–4.")
