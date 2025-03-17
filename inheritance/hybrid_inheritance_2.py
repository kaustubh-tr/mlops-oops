# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name: str) -> None:
        # Initialize the name attribute for all animals
        self.name = name

    def make_sound(self) -> None:
        # Generic method for all animals to make a sound
        print(f"{self.name} makes a sound.")

# Derived class 1 - Bird
class Bird(Animal):
    def __init__(self, name: str, can_fly: bool, **kwargs) -> None:
        # Added **kwargs to accept extra arguments (like can_swim) and pass them along
        # This makes Bird cooperative with multiple inheritance
        super().__init__(name, **kwargs)  # Pass name and any extra args to the next class in MRO
        self.can_fly = can_fly

    def fly(self) -> None:
        # Method to check and display flying capability
        if self.can_fly:
            print(f"{self.name} is flying.")
        else:
            print(f"{self.name} can't fly.")

# Derived class 2 - Fish
class Fish(Animal):
    def __init__(self, name: str, can_swim: bool, **kwargs) -> None:
        # Added **kwargs to accept extra arguments (like can_fly) and pass them along
        # This makes Fish cooperative with multiple inheritance
        super().__init__(name, **kwargs)  # Pass name and any extra args to the next class in MRO
        self.can_swim = can_swim

    def swim(self) -> None:
        # Method to check and display swimming capability
        if self.can_swim:
            print(f"{self.name} is swimming.")
        else:
            print(f"{self.name} can't swim.")

# Hybrid class - FlyingFish (inherits from both Bird and Fish)
class FlyingFish(Bird, Fish):
    def __init__(self, name: str, can_fly: bool, can_swim: bool) -> None:
        # Initialize FlyingFish by calling Bird's __init__, which chains through the MRO
        # MRO: FlyingFish -> Bird -> Fish -> Animal
        # super() ensures each class in the chain gets called exactly once
        super().__init__(name=name, can_fly=can_fly, can_swim=can_swim)
        # No need for explicit calls to Bird.__init__ and Fish.__init__
        # super() handles the delegation through the MRO

    def perform_actions(self) -> None:
        # Demonstrate both inherited abilities
        self.fly()   # From Bird class
        self.swim()  # From Fish class

# Create an instance of FlyingFish
flying_fish = FlyingFish("Flappy", True, True)

# Demonstrating hybrid inheritance
flying_fish.make_sound()       # Output: Flappy makes a sound.
flying_fish.perform_actions()  # Output: Flappy is flying. Flappy is swimming.

# Optional: Print the MRO to understand the inheritance order
print(FlyingFish.mro())        # Output: [FlyingFish, Bird, Fish, Animal, object]