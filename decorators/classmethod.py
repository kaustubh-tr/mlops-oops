# Initiate a class

class BankAccount:
    # Class variable shared across all instances
    bank_name = "MyBank"  # Bank's name for all instances
    
    def __init__(self, balance, account_holder):
        # self.__class__.bank_name = "ApnaBank"  # Direct way to change the class attribute (not recommendated)
        self.__balance = balance  # Private attribute for balance
        self._account_holder = account_holder  # Protected attribute for account holder name
    
    @classmethod
    def set_bank_name(cls, name):
        """Class method to set the bank name for all instances."""
        cls.bank_name = name  # This modifies the class-level variable
    
    @classmethod
    def get_bank_name(cls):
        """Class method to get the bank name."""
        return cls.bank_name  # This accesses the class-level variable
    
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

## Class Method:
# - A class method is a method that is bound to the class, rather than the instance.
# - It takes the class (`cls`) as its first parameter, which allows it to modify class-level variables/attributes (`bank_name` is this case).
# - Class methods are typically used to create factory methods or modify class-level data.

# Create objects
account1 = BankAccount(1000, "John Doe")
account2 = BankAccount(2000, "Jane Doe")

# Get bank name (class-level variable)
print(account1.get_bank_name())  # Output: MyBank
print(account2.get_bank_name())  # Output: MyBank

# Set new bank name using class method
BankAccount.set_bank_name("ApnaBank")

# Create a new account and check the updated bank name
account3 = BankAccount(1500, "Alice Smith")
print(account3.get_bank_name())  # Output: ApnaBank

# Get bank name directly from the class
print(BankAccount.get_bank_name())  # Output: ApnaBank
