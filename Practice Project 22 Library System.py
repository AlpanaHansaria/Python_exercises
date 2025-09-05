"""
22.	Simple Library System
o	Classes: Book, Library, User.
o	Borrow, return, check availability.
"""
class Library:

    books_available = {
        "The Great Gatsby": 5,
        "1984": 2,
        "To Kill a Mockingbird": 3,
        "Pride and Prejudice": 4,
        "The Catcher in the Rye": 3,
        "Moby Dick": 2,
        "The Hobbit": 6,
        "War and Peace": 2,
        "Harry Potter and the Sorcerer's Stone": 5,
        "The Lord of the Rings": 4,
        "The Chronicles of Narnia": 3,
        "Jane Eyre": 3,
        "The Odyssey": 2
    }

    @classmethod
    def show_menu(cls):
        print("\n--- Library System ---")
        print("1. View available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Check book availability")
        print("5. Exit")

    @classmethod
    def view_available_books(cls):
        print("Available books:")
        for book, quantity in cls.books_available.items():
            print(f" - {book}: {quantity} copies")

    @classmethod
    def borrow_book(cls):
        book_title = input("Enter the title of the book you want to borrow: ")
        if book_title in cls.books_available and cls.books_available[book_title] > 0:
            cls.books_available[book_title] -= 1
            print(f"You have borrowed '{book_title}'.")
        else:
            print(f"Sorry, '{book_title}' is not available.")
            
    @classmethod
    def return_book(cls):
        book_title = input("Enter the title of the book you want to return: ")
        if book_title in cls.books_available:
            cls.books_available[book_title] += 1
            print(f"You have returned '{book_title}'.")
        else:
            print(f"Sorry, '{book_title}' is not a part of this library.")

    @classmethod
    def check_book_availability(cls):
        book_title = input("Enter the title of the book to check availability: ")
        quantity = cls.books_available.get(book_title)

        if quantity is not None:
            print(f"'{book_title}' is available: {quantity} copies.")
        else:
            print(f"Sorry, '{book_title}' is not available in this library.")

    # Run the library system
    def run(cls):
        while True:
            cls.show_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                cls.view_available_books()
            elif choice == '2':
                cls.borrow_book()
            elif choice == '3':
                cls.return_book()
            elif choice == '4':
                cls.check_book_availability()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Run the library
library = Library()
library.run()