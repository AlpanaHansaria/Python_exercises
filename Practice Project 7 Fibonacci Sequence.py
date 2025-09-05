"""
7.	Fibonacci Sequence
o	Print first n numbers of Fibonacci series.
o	Bonus: Use recursion.
"""
def print_fibonacci_sequence(n):
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence():
    while True:
        user_input = input("Enter the number of Fibonacci numbers to print (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the Fibonacci Sequence Generator. Goodbye!")
            break
        try:
            print_fibonacci_sequence(int(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

 # Ask user if they want to continue
        while True:
            cont = input("\nDo you want to create another sequence? (y/n): ").lower()
            if cont == 'y':
                break  # Continue outer loop
            elif cont == 'n':
                print("Thanks for using the Fibonacci Sequence Generator! Goodbye!")
                return  # Exit the function completely
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Run the Fibonacci Sequence Generator
fibonacci_sequence()