#Home work assignment Class 5

"""
 Write a Python script that lets a user create and manage a to-do list. The program should allow the user to:
    1.	Add a new task to the list.
    2.	View all tasks currently in the list.
    3.	Mark a task as completed.
    4.	Delete a task from the list.
    5.	Save the tasks so that the list is not lost when the program closes.

 Bonus ideas (optional):
    1.	Show tasks in order of priority or due date.
    2.	Allow searching for tasks by keyword.
    3.	Display the number of pending vs completed tasks.

Goal: The script should use user-defined functions for each of the main actions (add, view, mark complete, delete) and 
    make use of built-in functions for tasks like input, printing, and list operations.
"""


# Simple list of tasks
tasks = ["Laundry", "Dishes", "Buy groceries", "Call mom", "Finish homework"]

#1.Adding new task "studying"
tasks.append("studying")

#2.View all tasks currently in the list.
print(tasks)

#3.Mark laundry as completed
tasks[0] = "Laundry completed"

#4.Delete laundry task from the list
previous_task = tasks.pop(0)

print(tasks)

# Open a file in write mode and save the tasks as a text file

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")  # Write each task on a new line


print("Tasks have been saved to tasks.txt!")

#Work on bonus ideas
#1.	Show tasks in order of priority or due date.
tasks = [
    {"desc": "Buy groceries", "priority": 'Average', "due": "2025-08-20", "status": "pending"},
    {"desc": "Finish homework", "priority": 'Low', "due": "2025-08-18", "status": "pending"},
    {"desc": "Do Laundry", "priority": 'Lowest', "due": "2025-08-10", "status": "completed"},
    {"desc": "Do dishes", "priority": 'High', "due": "2025-08-28", "status": "pending"},
    {"desc": "Call mom", "priority": 'Highest', "due": "2025-08-30", "status": "pending"}
]

#2. Allow searching for tasks by priority
def tasks_priority(priority):
    results = [task for task in tasks if task["priority"] == priority]
    return results
print("highest priority: ", tasks_priority('Highest'))

# Display tasks in order of due date
def tasks_due(due):
    results = [task for task in tasks if task["due"] == due]
    return results

print("Tasks due on 2025-08-30: ", tasks_due("2025-08-30"))

#3.	Display the number of pending vs completed tasks.
pending_tasks = sum(1 for task in tasks if task["status"] == "pending")
completed_tasks = sum(1 for task in tasks if task["status"] == "completed")     
print(f"Pending tasks: {pending_tasks}, Completed tasks: {completed_tasks}")    

