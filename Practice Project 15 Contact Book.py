"""
15.	Simple Contact Book
o	Store names and phone numbers in a dictionary.
o	Search, add, delete contacts.
"""
def contact_book():
    contacts = {
    "Alpana": 9083287626,
    "Archana": 7038635945,
    "Akash": 7325899240
    }

    while True:

        user_input = input("Enter 'Add', 'Delete', or 'View' for the contact book, or 'Exit' to exit the app: ")

        if user_input.lower() == "add":
            name = input("Enter the name to be added to the contact book: ")
            number = input("Enter the number to be added to the contact book: ")
            if not number.isdigit():
                print("Invalid number! Please enter digits only.")
                continue
            else:
                contacts[name] = int(number)
                print(f"{name} added to the contact book!")  
                print()  # extra line for readability

        elif user_input.lower() == "view":
            print("\nHere is the contact book: ")
            for name, number in contacts.items():
                print(f"{name}: {number}")      #for loop to print the contacts line-by-line
            print()  # extra line for readability
            
        elif user_input.lower() == "delete":
            name = input("Enter the name to delete: ")
            if name in contacts:
                contacts.pop(name)
                print(f"{name} deleted from the contact book!")
            else:
                print(f"{name} not found in the contact book!")

        elif user_input.lower() == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid input! Please enter 'Add', 'Delete', 'View', or 'Exit'.")


# Run the function
contact_book()