# Encapsulation

# Initiate a class
class BankAccount:
    def __init__(self, balance, account_holder):
        # Validate balance during initialization (no negative balance allowed)
        if balance < 0:
            raise ValueError("Balance can't be negative.")
        self.__balance = balance  # Private attribute (double underscore indicates private)
        self._account_holder = account_holder  # Protected attribute (single underscore for convention)
        self.account_type = "Savings"  # Public attribute

    def deposit(self, amount):
        # Ensure deposit amount is positive
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Ensure withdrawal doesn't exceed balance and is positive
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

    def get_balance(self):  # Getter method
        return self.__balance

    def set_balance(self, amount):  # Setter method
        # Set balance only if the amount is valid
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance can't be negative.")

# Create an object of BankAccount
account = BankAccount(1000, "John Doe")

# Accessing public attribute directly
print(account.account_type)  # Output: Savings

# Accessing protected attribute (not recommended, but still works)
print(account._account_holder)  # Output: John Doe

# Accessing private attribute directly will cause an AttributeError
# print(account.__balance)  # Uncommenting this would raise an error

# Deposit operation
account.deposit(500)
print(f"Balance after deposit: {account.get_balance()}")  # Output: 1500

# Withdraw operation
account.withdraw(200)  # Successful withdrawal
print(f"Balance after withdrawal: {account.get_balance()}")  # Output: 1300

# Withdraw operation with insufficient funds
account.withdraw(2000)  # Output: Insufficient funds.

# Using getter and setter to interact with the private attribute
account.set_balance(2000)
print(f"Balance after setting new balance: {account.get_balance()}")  # Output: 2000

# Name Mangling: Accessing the private attribute via the mangled name (not recommended)
print(account._BankAccount__balance)  # Output: 2000

# Example of Invalid Operation: Attempting to set a negative balance directly
# account.set_balance(-500)  # Output: Balance can't be negative.

# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP).
# It involves bundling the data (attributes) and the methods (functions) that operate on the data into a single unit, i.e., a class.
# Additionally, encapsulation restricts direct access to some of the object's attributes and methods to ensure data integrity and security.
# In Python, this is achieved using private, protected, and public access modifiers and getter/setter methods.
