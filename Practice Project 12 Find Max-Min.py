"""
12.	Find Maximum and Minimum
o	Input a list of numbers and output max and min values.
"""

def find_max_min():
    while True:
        try:
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

            if not numbers:
                print("You didn't enter any numbers. Please try again.")
                continue

        except ValueError:
            print("Invalid input! Please enter only numbers separated by spaces.")
            continue  # Ask for input again
    
        print("Maximum:", max(numbers))
        print("Minimum:", min(numbers))

        if input("Do you want to continue? (y for yes): ").lower() != "y":
            break

    print("Thanks for using the Max-Min Finder! Goodbye!")  # Goodbye message

# Run the function
find_max_min()