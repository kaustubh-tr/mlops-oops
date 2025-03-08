# Initiate a class

class BankAccount:
    def __init__(self, balance, account_holder):
        self.__balance = balance  # Private attribute (with double underscore)
        self._account_holder = account_holder  # Protected attribute (with single underscore)
        self.account_type = "Savings"  # Public attribute

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

# Create an object
account = BankAccount(1000, "John Doe")

# Print the id of the object
print(id(account))  # This will print the memory address of the 'account' object

# Accessing public attribute
print(account.account_type)  # Output: Savings

# Accessing protected attribute (can be accessed, but not recommended)
print(account._account_holder)  # Output: John Doe

# Accessing private attribute (should not be accessed directly outside the class)
# print(account.__balance)  # This would raise an AttributeError

account.deposit(500)

# Using getter and setter to interact with the private attribute
print(account.get_balance())  # Output: 1500
account.set_balance(2000)
print(account.get_balance())  # Output: 2000

## Name Mangling
# Accessing the private attribute using the mangled name (not recommended as it breaks the encapsulation principle)
print(account._BankAccount__balance)  # Output: 2000
