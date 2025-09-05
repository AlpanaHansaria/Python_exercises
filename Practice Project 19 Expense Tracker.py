"""
19.	Expense Tracker
o	Input daily expenses.
o	Save them to a file and calculate total.
"""
# Simple Expense Tracker

import os

# Set working directory
os.chdir(r"c:/Users/Alpan/OneDrive/Documents/GitHub/Python_exercises")
print("Current working directory:", os.getcwd())

# Categories
categories = ["Food", "Transport", "Utilities", "Entertainment", "Other"]

# Dictionary to store expenses
expenses = {cat: [] for cat in categories}

# Main loop
while True:
    print("\nCategories: " + ", ".join(categories))
    cat = input("Enter category (or 'done' to finish): ").title()
    if cat.lower() == "done":
        break
    if cat not in categories:
        print("Invalid category. Try again.")
        continue
    try:
        amt = float(input("Enter amount: "))
        expenses[cat].append(amt)
    except ValueError:
        print("Please enter a number.")
        continue

    # Ask if user wants to add more
    more = input("Add more expenses? (y/n): ").lower()
    if more == "n":
        break

# Save to file
file_path = "expenses.txt"
with open(file_path, "w") as f:
    for cat, amts in expenses.items():
        f.write(f"{cat}:\n")
        for amt in amts:
            f.write(f"  - {amt}\n")

# Print expenses
print("\nYour expenses:")
total = 0
for cat, amts in expenses.items():
    print(f"\n{cat}:")
    if amts:
        for amt in amts:
            print(f"  - {amt}")
            total += amt
    else:
        print("  - None")

print(f"\nTotal expenses: {total}")
print(f"Expenses saved to '{file_path}'.")
