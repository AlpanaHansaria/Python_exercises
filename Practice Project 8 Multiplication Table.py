"""
8.	Multiplication Table
o	Print multiplication table for a given number using loops.
"""

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def multiplication_table():
    while True:
        user_input = input("Enter a number to print its multiplication table (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the Multiplication Table Generator. Goodbye!")
            break
        try:
            print_multiplication_table(int(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

 # Ask user if they want to continue
        while True:
            cont = input("\nDo you want to create another multiplication Table? (y/n): ").lower()
            if cont == 'y':
                break  # Continue outer loop
            elif cont == 'n':
                print("Thanks for using the Multiplication Table Generator! Goodbye!")
                return  # Exit the function completely
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Run the Multiplication Table Generator
multiplication_table()
