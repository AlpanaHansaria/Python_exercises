"""
4.	Simple Interest Calculator
o	Input: principal, rate, time. Output: simple interest.
"""
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def simple_interest_calculator():
    while True:
        expr = input("Enter principal, rate, and time (comma-separated) or 'exit': ")
        if expr.lower() == 'exit':
            print("Exiting the Simple Interest Calculator. Goodbye!")
            break

        try:
            principal, rate, time = map(float, expr.split(','))
            interest = calculate_simple_interest(principal, rate, time)
            print(f"Simple Interest: {interest}")
        except ValueError:
            print("Invalid input! Please enter numbers in the format: principal, rate, time")

        # Ask user if they want to continue
        while True:
            cont = input("\nDo you want to calculate another interest? (y/n): ")
            if cont.lower() == 'y':
                break  # Continue outer loop
            elif cont.lower() == 'n':
                print("Thanks for using the Simple Interest Calculator! Goodbye!")
                return  # Exit the function completely
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Run the calculator
simple_interest_calculator()
