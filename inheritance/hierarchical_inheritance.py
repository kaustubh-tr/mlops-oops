# Hierarchical Inheritance
# In hierarchical inheritance, multiple classes inherit from a single base class.

# Base class
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        print(f"{self.name} makes a sound.")

    def __str__(self) -> str:
        return f"Animal({self.name})"

# Derived class 1 - Dog
class Dog(Animal):
    def speak(self) -> None:
        print(f"{self.name} barks.")

    def __str__(self) -> str:
        return f"Dog({self.name})"

# Derived class 2 - Cat
class Cat(Animal):
    def speak(self) -> None:
        print(f"{self.name} meows.")

    def __str__(self) -> str:
        return f"Cat({self.name})"

# Derived class 3 - Cow
class Cow(Animal):
    def speak(self) -> None:
        print(f"{self.name} moos.")

    def __str__(self) -> str:
        return f"Cow({self.name})"

# Create instances of each derived class
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("MooMoo")

# Demonstrating polymorphism: each animal speaks in its own way
dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.
cow.speak()  # Output: MooMoo moos.

# Print object representation using __str__()
print(dog)   # Output: Dog(Buddy)
print(cat)   # Output: Cat(Whiskers)
print(cow)   # Output: Cow(MooMoo)
