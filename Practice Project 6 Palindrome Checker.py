"""
6.	Palindrome Checker
o	Input a string and check if it reads the same backward.
o	Bonus: Ignore spaces and capitalization.
"""
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = s.replace(" ", "").lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

def palindrome_checker():
    while True:
        user_input = input("Enter a string to check if it's a palindrome (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the Palindrome Checker. Goodbye!")
            break

        if is_palindrome(user_input):
            print("It's a palindrome!")
        else:
            print("It's not a palindrome.")

        # Ask user if they want to continue
        while True:
            cont = input("\nDo you want to check another string? (y/n): ").lower()
            if cont == 'y':
                break  # Continue outer loop
            elif cont == 'n':
                print("Thanks for using the Palindrome Checker! Goodbye!")
                return  # Exit the function completely
            else:
                print("Invalid input! Please enter 'y' for yes or 'n' for no.")

# Run the Palindrome Checker
palindrome_checker()