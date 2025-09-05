"""
1.	Simple Calculator
o	Perform addition, subtraction, multiplication, division.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result is: ", a + b)
elif operation == "-":
    print("Result is: ", a - b)
elif operation == "*":
    print("Result is: ", a * b)
elif operation == "/":
    print("Result is: ", a / b)
else:
    print("Invalid operation")
"""
""" Advanced Calculator

o	Bonus: Allow multiple operations in a single session.
o	Bonus: Handle invalid inputs gracefully.
"""

# Advanced Calculator - multiple operations in a single session
# Safe Advanced Calculator with +, -, *, /, (), and power **
import operator

# Allowed operators
allowed_operators = {'+', '-', '*', '/', '(', ')', '**', '.', ' '}

def is_valid_expression(expr):
    """Check if the expression contains only allowed characters."""
    for char in expr:
        if not char.isdigit() and char not in allowed_operators:
            return False
    return True

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("You can type expressions like (5 + 3) * 2 ** 2 / 4")
    print("Type 'exit' to quit.\n")

    while True:
        expr = input("Enter expression: ")
        if expr.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        # Check if expression is safe
        if not is_valid_expression(expr):
            print("Invalid input! Only numbers, +, -, *, /, (), **, and . are allowed.")
            continue
        
        try:
            # Evaluate the expression safely
            result = eval(expr)
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero!")
        except Exception as e:
            print("Error: Invalid expression. Details:", e)

# Run the calculator
calculator()