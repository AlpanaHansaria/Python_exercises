"""
11.	To-Do List
o	Add, remove, view tasks stored in a list.
o	Bonus: Save tasks in a file.
"""

"""
11. To-Do List
o Add, remove, view tasks stored in a list.
o Bonus: Save tasks in a file.
"""

import os

# File to store tasks
FILE_NAME = "C:\\Users\\Alpan\\OneDrive\\Documents\\GitHub\\Python_exercises\\tasks.txt"

# Check if file exists; if not, create it
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass  # just create an empty file

# Load tasks from file
with open(FILE_NAME, "r") as f:
    tasks = [line.strip() for line in f.readlines()]

def save_tasks():
    """Save the current tasks to a file"""
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks()  # Save after adding
    print(f"'{task}' added to the list!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks()  # Save after removing
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1–4.")
