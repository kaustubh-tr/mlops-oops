# Single or Basic Inheritance:
# A child class inherits from a parent class, allowing it to reuse code from the parent and extend or modify it.

# Base class (Parent class)
class Parent:
    def __init__(self, name, occupation):
        # Initialize the name and occupation attributes for the Parent class
        self.name = name
        self.occupation = occupation

    def greet(self):
        # Method in Parent class: Greets the user using the name and occupation attributes
        print(f"Hello, my name is {self.name} and I am a {self.occupation}.")

# Derived class (Child class) inherits from Parent class
class Child(Parent):
    # The Child class has additional methods and attributes not found in the Parent class
    def __init__(self, name, age, grade, hobby, occupation):
        # Use super() to call the Parent's __init__ method and initialize 'name' and 'occupation'
        super().__init__(name, occupation)
        # Initialize the child-specific attributes
        self.age = age
        self.grade = grade
        self.hobby = hobby

    def greet(self):
        # Using super() to call the greet method from the Parent class
        super().greet()
        # Extend the greet method to include the child's age, grade, and hobby
        print(f"I am {self.age} years old, in grade {self.grade}, and I love {self.hobby}.")

    def play(self):
        # Method in Child class: Describes the child playing
        print(f"{self.name} is playing.")

# Create an instance of the Child class
child = Child("Alice", 10, 5, "painting", "teacher")

# The Child instance can access the greet method from the Parent class using super()
child.greet()  # Output:
               # Hello, my name is Alice and I am a teacher.
               # I am 10 years old, in grade 5, and I love painting.
print()
# The Child instance can also access its own play method
child.play()   # Output: Alice is playing.
