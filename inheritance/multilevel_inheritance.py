# Multilevel Inheritance:
# A child class inherits from a parent class, which in turn inherits from a grandparent class, forming a hierarchy.

# Base class (Grandparent class)
class Grandparent:
    def __init__(self, name, country):
        # Initialize the name and country attributes for the Grandparent class
        self.name = name
        self.country = country

    def greet(self):
        print(f"Hello, I am {self.name} from {self.country}.")

# Dervied class (Parent class) inherits from Grandparent class
class Parent(Grandparent):
    def __init__(self, name, country, occupation):
        # Use super() to call the Grandparent's __init__ method and initialize 'name' and 'country'
        super().__init__(name, country)
        # Initialize the occupation attribute for the Parent class
        self.occupation = occupation

    def greet(self):
        # Using super() to call the greet method from the Grandparent class
        super().greet()
        # Extend the greet method to include the parent's occupation
        print(f"I am a {self.occupation}.")

# Derived class (Child class) inherits from Parent class
class Child(Parent):
    def __init__(self, name, country, occupation, age, hobby):
        # Use super() to call the Parent's __init__ method and initialize 'name', 'country' and 'occupation'
        super().__init__(name, country, occupation)
        # Initialize the child-specific attributes: age and hobby
        self.age = age
        self.hobby = hobby

    def greet(self):
        # Using super() to call the greet method from the Parent class
        super().greet()
        # Extend the greet method to include the child's age and hobby
        print(f"I am {self.age} years old, and I love playing {self.hobby}.")

# Create an instance of the Child class
child = Child("John", "India", "Software Engineer", 25, "cricket")

# The Child instance can access the greet method from the Grandparent class via the Parent class using super()
child.greet()  
# Output:
# Hello, I am John from India.
# I am a Software Engineer.
# I am 25 years old, and I love playing cricket.
