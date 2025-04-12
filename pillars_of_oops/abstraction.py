# Abstraction is the concept of hiding complex implementation details and showing only the necessary features to the user.

# Import ABC (Abstract Base Class) and abstractmethod decorator
from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    # Abstract method (no implementation here)
    @abstractmethod
    def sound(self):  # I don't know HOW, but sound method MUST exist
        pass
    
    @abstractmethod
    def move(self):  # I don't know HOW, but move method MUST exist
        pass
    
    # Regular method
    def sleep(self):
        print(f"The {self.__class__.__name__.lower()} is sleeping")

# Concrete Class 1 - Dog
class Dog(Animal):
    def sound(self):  # Defining sound method for Dog
        print("Dog says: Woof Woof!")
    
    def move(self):  # Defining move method for Dog
        print("Dog is running!")

# Concrete Class 2 - Cat
class Cat(Animal):
    def sound(self):  # Defining sound method for Cat
        print("Cat says: Meow Meow!")
    
    def move(self):  # Defining move method for Cat
        print("Cat is jumping!")

# Concrete Class 3 - Bird
class Bird(Animal):
    def sound(self):  # Defining sound method for Bird
        print("Bird says: Chirp Chirp!")
    
    def move(self):  # Defining move method for Bird
        print("Bird is flying!")

# Creating objects of the concrete classes
dog = Dog()
cat = Cat()
bird = Bird()

# Calling the methods
dog.sound()   # Output: Dog says: Woof Woof!
dog.move()    # Output: Dog is running!
dog.sleep()   # Output: The dog is sleeping
print()
cat.sound()   # Output: Cat says: Meow Meow!
cat.move()    # Output: Cat is jumping!
cat.sleep()   # Output: The cat is sleeping
print()
bird.sound()  # Output: Bird says: Chirp Chirp!
bird.move()   # Output: Bird is flying!
bird.sleep()  # Output: The bird is sleeping

# An abstract class in Python cannot be instantiated directly. It acts as a template (or blueprint) for other classes.
# Abstract classes are used when you want to define a common interface (i.e., a set of methods) that subclasses must implement.

# @abstractmethod is a decorator that marks a method as abstract.
# This means that any class that inherits from this class must override the abstract method.
# If a subclass does not implement this method, Python will raise an error.
# Think of it as creating a contract: the subclass must follow the blueprint.

# Why use @abstractmethod?
# You’re saying: “Hey subclass! You can’t skip this method. You must define it if you want to be used.”
# It enforces that certain methods must be present in any class that inherits from the abstract base class.
