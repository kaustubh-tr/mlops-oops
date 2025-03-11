# Initiate a class

class BankAccount:
    def __init__(self, balance, account_holder):
        self.__balance = balance  # Private attribute for balance
        self._account_holder = account_holder  # Protected attribute for account holder name
    
    @property
    def balance(self):
        """Property method to get the balance."""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter method for balance to ensure it's not negative."""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance can't be negative.")

    @property
    def account_details(self):
        """Property method to get a description of the account."""
        return f"Account Holder: {self._account_holder}, Balance: {self.__balance}"

    @account_details.setter
    def account_details(self, details):
        """Setter for account details."""
        name, balance = details.split(", ")
        self._account_holder = name.split(": ")[1]
        self.__balance = float(balance.split(": ")[1])


## Property:
# - The property decorator allows us to define methods that behave like attributes.
# - We can create getter and setter methods using `@property` and `@<property_name>.setter`.
# - This is useful for controlling how attributes are accessed and modified, while keeping the code clean.

# Create an account
account1 = BankAccount(1000, "John Doe")

# Using the property to get balance
print(account1.balance)  # Output: 1000

# Using the setter to modify the balance
account1.balance = 1200  # Valid update
print(account1.balance)  # Output: 1200

# Trying to set a negative balance
account1.balance = -500  # Output: Balance can't be negative.

# Using the property to get account details
print(account1.account_details)  # Output: Account Holder: John Doe, Balance: 1200

# Using the setter to update account details
account1.account_details = "Account Holder: Jane Doe, Balance: 2500"

# Check updated account details
print(account1.account_details)  # Output: Account Holder: Jane Doe, Balance: 2500.0
