# Multiple Inheritance (Diamond Problem)
# In multiple inheritance, a class can inherit from more than one class.
# The Method Resolution Order (MRO) determines the order in which methods are inherited and called.

# Common Base class
class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}.")

# Intermediate class
class B(A):

    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()  # Calls the next class in the MRO

# Intermediate class
class C(A):

    def greet(self):
        print(f"Hello from C, {self.name}.")
        super().greet()  # Calls the next class in the MRO

# Derived class
class D(B, C):

    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet()  # Calls the next class in the MRO


# Create an instance of D
d = D("John")
d.greet()

## Output:
# Hello from D, John.
# Hello from B, John.
# Hello from C, John.
# Hello from A, John.

## Explanation of MRO (Method Resolution Order):
# Python follows the C3 Linearization algorithm to determine the MRO.
# The MRO for class D is: D -> B -> C -> A -> object.
# This means the method lookup follows this order when calling super():
# 1. D.greet() is called first (because D is the first class in the MRO).
# 2. Then, B.greet() is called via super() inside D.greet().
# 3. Next, C.greet() is called via super() inside B.greet().
# 4. Finally, A.greet() is called via super() inside C.greet().
# This is why the output appears in the following order.