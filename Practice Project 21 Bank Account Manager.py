"""
21.	Bank Account Manager
o	Create Account class with deposit, withdraw, balance check.
o	Bonus: Add interest calculation.
"""

class AccountManager:

    def __init__(self, balance, rate, time):
        self.balance = balance
        self.rate = rate
        self.time = time
    
    def show_menu(self):
        print("\n--- Bank Account Manager ---")
        print("1. View balance")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Interest Calculation")
        print("5. Exit")

    def view_balance(self):
        
        print(f"Your current balance is: {self.balance}")

    def deposit(self):
        try:
            # Take input for the amount to be deposited
            self.depo = float(input("Enter the amount to be deposited: "))

            if self.depo < 0:
                print("Error: Deposit amount cannot be negative.")

            else:
                self.balance += self.depo
                print(f"Amount Deposited: {self.depo}")

        except ValueError:
            print("Enter a valid number for deposit.")

    def withdraw(self):
        try:
            # Take input for the amount to withdraw
            self.withdrawal = float(input("Enter the amount to withdraw today: "))

            if self.withdrawal < 0:
                print("Error: Withdrawal amount cannot be negative.")

            elif self.withdrawal > self.balance:
                print("Insufficient funds.")

            else:
                self.balance -= self.withdrawal
                print(f"Amount Withdrawn: {self.withdrawal}")

        except ValueError:
            print("Enter a valid number for withdrawal.")


    def interest_calc(self, rate, time):
        self.interest = (self.balance * rate/100 * time)
        self.balance += self.interest
        
        print(f"Interest: {self.interest}")
        print(f"New Balance: {self.balance}")



    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.view_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                interest_rate = float(input("Enter the interest rate you get from your bank: "))
                time = float(input("Enter number of years for the interest calculation: "))
                self.interest_calc(interest_rate, time)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Example usage
AccountManager(10000, 0, 0).run()