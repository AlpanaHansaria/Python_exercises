"""
3.	Even/Odd Checker
o	Take input from user and tell whether the number is even or odd.
o	Bonus: Check a range of numbers.
"""
def is_valid_number(expr):
    """Check if the expression contains only numbers."""
    return expr.isdigit()

def check_even_odd():
    while True:
        choice = input("\nDo you want to check a single number or a range? (number/range/exit): ").lower()
        
        if choice == "exit":
            print("Exiting the Even/Odd Checker. Goodbye!")
            break

        elif choice == "number":
            expr = input("Enter a number: ")
            if not is_valid_number(expr):
                print("Invalid input! Only numbers are allowed.")
                continue

            number = int(expr)
            if number % 2 == 0:
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")  

        elif choice == "range":
            expr = input("Enter a range (e.g., 1-10): ")
            try:
                start, end = map(int, expr.split('-'))
            except ValueError:
                print("Invalid input! Enter the range like 1-10.")
                continue

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(f"{num} is even.")
                else:
                    print(f"{num} is odd.")

        else:
            print("Invalid choice! Please type 'number', 'range', or 'exit'.")
            continue

        # Ask user if they want to continue
        while True:
            cont = input("\nDo you want to check another number or range? (y/n): ").lower()
            if cont == 'y':
                break  # Continue outer loop
            elif cont == 'n':
                print("Thanks for using the Even/Odd Checker! Goodbye!")
                return  # Exit the function completely
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Run the checker
check_even_odd()
