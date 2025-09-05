"""
25.	Basic Inventory Management
o	Class Product with name, quantity, price.
o	Add, remove, update stock.
"""
class InventoryManagement:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_stock(self, amount):
        self.quantity += amount
        print(f"Added {amount} of {self.name}. New quantity: {self.quantity}")

    def remove_stock(self, amount):
        if amount > self.quantity:
            print("Not enough stock to remove.")
        else:
            self.quantity -= amount
            print(f"Removed {amount} of {self.name}. New quantity: {self.quantity}")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Updated price of {self.name}. New price: {self.price}")

# Run
product1 = InventoryManagement("Laptop", 10, 999.99)
product1.add_stock(5)
product1.remove_stock(3)
product1.update_price(899.99)