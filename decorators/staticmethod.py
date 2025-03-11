# Initiate a class

class BankAccount:
    # Static or Class variable/attribute
    # Static variables are shared across all instances of the class.
    # This is useful when we want to maintain a state that should be consistent across all instances, like tracking user IDs.
    
    __user_id = 1  # Static variable to keep track of the user ID

    def __init__(self, balance, account_holder):
        self.id = BankAccount.__user_id  # Assign the current ID to the account
        BankAccount.__user_id += 1  # Increment the static user ID for the next account
        self.__balance = balance  # Private attribute
        self._account_holder = account_holder  # Protected attribute
        self.account_type = "Savings"  # Public attribute
    
    @staticmethod
    def get_id():
        return BankAccount.__user_id  # Static method to get the current ID
    
    @staticmethod
    def set_id(val):
        BankAccount.__user_id = val  # Static method to set a new ID
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):  # Getter method
        return self.__balance

    def set_balance(self, amount):  # Setter method
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance can't be negative.")

    @staticmethod
    def bank_info():  # Static method
        print(f"Welcome to {BankAccount.bank_name}! We offer savings and checking accounts.")
    
## Static Method:
# - Methods at class level are called static method. It belongs to the class rather than to an instance of the class. Used as a decorator.
# - It doesn't require a reference to a specific instance (no 'self' parameter).
# - Static methods are typically used for operations that are related to the class itself, but not specific to any particular instance.
# - Its common for whole the class, will not be created everytime.

## Advantage of static method:
# - It can be called on the class itself (e.g., BankAccount.get_id()) without needing an instance.
# - It is often used for utility functions, helper methods, or when we need a method to operate at the class level rather than the instance level.

## Why 'self' is not passed:
# - Static methods do not require access to instance-specific data (like attributes), so they do not take 'self' as a parameter.
# - They are meant to work with class-level data or perform actions that are not related to a specific instance.

# Create objects
account1 = BankAccount(1000, "John Doe")
account2 = BankAccount(2000, "Jane Doe")
account3 = BankAccount(1500, "Alice Smith")

# Access each account's id
print(account1.id)  # Output: 1
print(account2.id)  # Output: 2
print(account3.id)  # Output: 3

# Get the next user ID (should be 4 after 3 accounts)
print(BankAccount.get_id())  # Output: 4

# Set the user ID to a custom value
BankAccount.set_id(100)

# Create a new account and see the new ID
account4 = BankAccount(1200, "Bob Brown")
print(account4.id)  # Output: 100 (since we manually set the user ID to 100)

# Get the next user ID (should be 101)
print(BankAccount.get_id())  # Output: 101

# Note: static method can't access or modify class state and generally for utility