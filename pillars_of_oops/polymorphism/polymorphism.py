# Polymorphism

# Base class: Animal
class Animal:
    # Constructor to initialize the name of the animal
    def __init__(self, name):
        self.name = name
    
    # Base method: This method is intended to be overridden
    def sound(self):
        print(f"{self.name} makes a sound")

    # General method for movement, also overridden in subclasses
    def move(self):
        print(f"{self.name} is moving.")

# Subclass: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # Initialize using the parent class constructor
        super().__init__(name)
        self.breed = breed
    
    # Polymorphic behavior: Overriding sound method
    def sound(self):
        print(f"{self.name} (a {self.breed}) says: Woof Woof!")
    
    # Polymorphic behavior: Overriding move method
    def move(self):
        print(f"{self.name} (a {self.breed}) runs around excitedly!")

# Subclass: Cat
class Cat(Animal):
    def __init__(self, name, color):
        # Initialize using the parent class constructor
        super().__init__(name)
        self.color = color
    
    # Polymorphic behavior: Overriding sound method
    def sound(self):
        print(f"{self.name} (a {self.color} cat) says: Meow Meow!")
    
    # Polymorphic behavior: Overriding move method
    def move(self):
        print(f"{self.name} (a {self.color} cat) gracefully jumps!")

# Subclass: Bird
class Bird(Animal):
    def __init__(self, name, species):
        # Initialize using the parent class constructor
        super().__init__(name)
        self.species = species
    
    # Polymorphic behavior: Overriding sound method
    def sound(self):
        print(f"{self.name} (a {self.species}) says: Chirp Chirp!")
    
    # Polymorphic behavior: Overriding move method
    def move(self):
        print(f"{self.name} (a {self.species}) flies in the sky!")

# Function that demonstrates polymorphism
def make_animal_sound(animal: Animal):
    """
    This function demonstrates polymorphism.
    It accepts any object of type Animal (or subclass of Animal) and calls the sound() method.
    Since different animals have different implementations of sound(), the output will vary.
    """
    print(f"{animal.name} is an animal:")
    animal.sound()  # Calls the overridden sound method based on the actual object type
    animal.move()   # Calls the overridden move method based on the actual object type
    print()

# Create objects of different animal subclasses
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="Black")
bird = Bird(name="Tweety", species="Canary")

# Demonstrating polymorphism by calling the same function for different objects
make_animal_sound(dog)   # Output: Buddy (a Golden Retriever) says: Woof Woof!
make_animal_sound(cat)   # Output: Whiskers (a Black cat) says: Meow Meow!
make_animal_sound(bird)  # Output: Tweety (a Canary) says: Chirp Chirp!

# Polymorphism is an OOP concept that means "many forms".
# In Python, it allows objects of different classes to be treated as objects of a common superclass.
# This is especially useful when you have different types of objects that share a common interface or behavior.
