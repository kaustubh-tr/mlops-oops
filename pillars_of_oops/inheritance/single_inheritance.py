# Single or Basic Inheritance:
# A child class inherits from a parent class, allowing it to reuse code from the parent and extend or modify it.

# Base class (Parent class)
class Parent:
    def __init__(self, name, occupation):
        # Initialize the name and occupation attributes for the Parent class
        self.name = name
        self.occupation = occupation

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def work(self):
        print(f"{self.name} is working as a {self.occupation}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Derived class (Child class) inherits from Parent class
class Child(Parent):
    # The Child class has additional methods and attributes not found in the Parent class
    def __init__(self, name, age, hobby, occupation):
        # Use super() to call the Parent's __init__ method and initialize 'name' and 'occupation'
        super().__init__(name, occupation)
        # Initialize the child-specific attribute 'age'
        self.age = age
        self.hobby = hobby

    def greet(self):
        # Using super() to call the greet method from the Parent class
        super().greet()
        print(f"I am {self.age} years old.")

    def play(self):
        print(f"{self.name} is enjoying {self.hobby}.")

    def study(self):
        print(f"{self.name} is studying hard.")

# Create an instance of the Child class
child = Child("Alice", 20, "coding", "Data Scientist")

# The Child instance can access the greet method from the Parent class using super()
child.greet()  
# Output: 
# Hello, my name is Alice.
# I am 20 years old.

# The Child instance can also access its own play method
child.play()   # Output: Alice is enjoying coding.

# The Child instance can also access methods from the Parent class
child.work()   # Output: Alice is working as a Data Scientist.
child.sleep()  # Output: Alice is sleeping.

# The Child instance can access its own study method
child.study()  # Output: Alice is studying hard.
