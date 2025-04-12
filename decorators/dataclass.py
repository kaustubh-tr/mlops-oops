# Importing the dataclass decorator from the dataclasses module
from dataclasses import dataclass

# Step 1: Basic @dataclass usage
# The @dataclass decorator automatically generates special methods for the class, such as __init__(), __repr__(), __eq__(), and __hash__().

@dataclass
class Person:
    name: str  # attribute type 'str'
    age: int   # attribute type 'int'

# Now, let's create an instance of the Person class
person1 = Person(name="Alice", age=30)

# The __init__() method is automatically created, so we can instantiate the class like this
print(person1)  # Output: Person(name='Alice', age=30)
# It automatically prints the __repr__() method

# Step 2: The generated methods
# We can see that __repr__ is automatically created for us:
print(f"Person1 -> {person1}")  # Output: Person1 -> Person(name='Alice', age=30)

# We can also compare instances using the __eq__ method:
person2 = Person(name="Alice", age=30)
print(f"person1 == person2: {person1 == person2}")  # Output: True

# If we modify one attribute, __eq__() will return False:
person2.age = 31
print(f"person1 == person2: {person1 == person2}")  # Output: False

# Step 3: Using default values for fields
# We can define default values for fields, just like any other class variable.

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0  # Default value for 'quantity' field

product1 = Product(name="Laptop", price=1200.00)
print(product1)  # Output: Product(name='Laptop', price=1200.0, quantity=0)

# If we don't provide the 'quantity' argument, it will default to 0.

# Step 4: Post-init processing
# Sometimes we need to perform extra processing after the object is initialized.
# The __post_init__() method can be used for that purpose.

@dataclass
class Rectangle:
    width: int
    height: int

    def __post_init__(self):
        # After the object is created, we can perform additional checks or calculations
        self.area = self.width * self.height

rectangle = Rectangle(width=5, height=3)
print(f"Area of rectangle: {rectangle.area}")  # Output: Area of rectangle: 15

# Step 5: Frozen dataclasses (Immutable Objects)
# If we want to make your dataclass immutable (i.e., fields can't be modified after object creation),
# we can use the 'frozen=True' parameter.

@dataclass(frozen=True)
class Employee:
    name: str
    position: str
    salary: float

# This class is immutable, and trying to modify its attributes will raise an error
employee = Employee(name="John", position="Manager", salary=85000)
# The following line would raise an error:
# employee.name = "Jane"  # Uncommenting this line will raise: FrozenInstanceError

# Step 6: Comparing dataclasses with custom fields (custom __eq__ method)

# By default, @dataclass generates __eq__ to compare field values.
# However, we can provide a custom __eq__ method for more advanced logic if needed.

@dataclass
class BankAccount:
    account_number: int
    balance: float

    def __eq__(self, other):
        # Custom equality check: considering only account_number for equality
        if isinstance(other, BankAccount):
            return self.account_number == other.account_number
        return False

account1 = BankAccount(account_number=123456, balance=500.0)
account2 = BankAccount(account_number=123456, balance=1500.0)
account3 = BankAccount(account_number=789012, balance=1500.0)

print(f"account1 == account2: {account1 == account2}")  # Output: True (same account_number)
print(f"account1 == account3: {account1 == account3}")  # Output: False (different account_number)

# Step 7: Additional Features of @dataclass

# The @dataclass decorator can also be used with the following features:
# - Default factory for mutable types (e.g., list, dict)
# - Ordering (comparison methods like __lt__, __gt__, etc.)

@dataclass(order=True)
class Task:
    description: str
    priority: int  # Lower number means higher priority

# We can now compare Task objects based on the 'priority' field:
task1 = Task(description="Finish MLOps pipeline", priority=1)
task2 = Task(description="Fix bug", priority=2)

print(f"Is task1 higher priority than task2? {task1 < task2}")  # Output: True

# Example of using default_factory for a mutable type (list):
from dataclasses import field

@dataclass
class Project:
    name: str
    contributors: list = field(default_factory=list)  # Using default_factory to avoid mutable default

project = Project(name="MLOps")
project.contributors.append("Alice")
project.contributors.append("Bob")

print(f"Project Contributors: {project.contributors}")  # Output: Project Contributors: ['Alice', 'Bob']
