# Hybrid Inheritance
# Hybrid Inheritance is a type of inheritance where a class combines multiple inheritance types

# Base class
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self) -> None:
        print(f"{self.name} makes a sound.")

# Derived class 1 - Bird
class Bird(Animal):
    def __init__(self, name: str, can_fly: bool, can_swim: bool) -> None:
        # super().__init__(name)  # Use super() to call Animal's constructor if directly Bird() is called
        super().__init__(name, can_swim)  # Use super() to call Fish's constructor if FlyingFish() is called
        self.can_fly = can_fly

    def fly(self) -> None:
        if self.can_fly:
            print(f"{self.name} is flying.")
        else:
            print(f"{self.name} can't fly.")

# Derived class 2 - Fish
class Fish(Animal):
    def __init__(self, name: str, can_swim: bool) -> None:
        super().__init__(name)  # Use super() to call Animal's constructor
        self.can_swim = can_swim

    def swim(self) -> None:
        if self.can_swim:
            print(f"{self.name} is swimming.")
        else:
            print(f"{self.name} can't swim.")

# Hybrid class - FlyingFish (inherits from both Bird and Fish)
class FlyingFish(Bird, Fish):
    def __init__(self, name: str, can_fly: bool, can_swim: bool) -> None:
        # Initialize FlyingFish by calling Bird's __init__, which chains through the MRO
        # MRO: FlyingFish -> Bird -> Fish -> Animal
        # Explicit constructor calling for both Bird and Fish
        Bird.__init__(self, name, can_fly, can_swim)  # Initialize Bird (explicit call)
        Fish.__init__(self, name, can_swim)  # Initialize Fish (explicit call)

    def perform_actions(self) -> None:
        self.fly()   # From Bird class
        self.swim()  # From Fish class

# Create an instance of FlyingFish
flying_fish = FlyingFish("Flappy", True, True)

# Demonstrating hybrid inheritance
flying_fish.make_sound()       # Output: Flappy makes a sound.
flying_fish.perform_actions()  # Output: Flappy is flying. Flappy is swimming.

print(FlyingFish.__mro__)
print(FlyingFish.mro())

# You’d think super().__init__(name) calls Animal.__init__ because Bird inherits from Animal, right?
# That’s true if Bird were alone (like if you made a Bird instance directly).
# But here, self is a FlyingFish object, and that changes everything.
# super() doesn’t just look at the class it’s written in (Bird) and its direct parent (Animal).
# Instead, it looks at the MRO of the instance’s class (here, FlyingFish) and finds the next class after the one calling it.
# So:
# Class calling super(): Bird.
# MRO of self (a FlyingFish instance): FlyingFish -> Bird -> Fish -> Animal.
# Next class after Bird in the MRO: Fish.
# That’s why super().__init__(name) in Bird.__init__ calls Fish.__init__ when self is a FlyingFish object!
