# Operator Overloading (A type of Polymorphism)

# Operator overloading is a type of polymorphism where we define or change the behavior
# of standard operators (like +, -, *, ==, etc.) for user-defined classes.

# In Python, this is done by defining special methods (also called "magic" or "dunder" methods)
# such as __add__, __sub__, __eq__, __str__, and so on.

class ComplexNumber:
    def __init__(self, real, img):
        # Constructor to initialize the complex number with real and imaginary parts
        self.real = real  # Real part of the complex number
        self.img = img    # Imaginary part of the complex number

    def display_number(self):
        # Display the complex number in the form of a + bi
        print(f"{self.real} + {self.img}i")

    def add(self, num2):
        # Add two complex numbers
        real_ = self.real + num2.real
        img_ = self.img + num2.img
        return ComplexNumber(real_, img_)
    
    def sub(self, num2):
        # Subtract one complex number from another
        real_ = self.real - num2.real
        img_ = self.img - num2.img
        return ComplexNumber(real_, img_)
    
    def mul(self, num2):
        # Multiply two complex numbers using the formula:
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_ = self.real * num2.real - self.img * num2.img
        img_ = self.real * num2.img + self.img * num2.real
        return ComplexNumber(real_, img_)
    
    def div(self, num2):
        # Divide two complex numbers using the formula:
        # (a + bi) / (c + di) = ((a + bi)(c - di)) / (c^2 + d^2)
        denom = num2.real**2 + num2.img**2
        if denom == 0:
            raise ValueError("Cannot divide by zero")
        real_ = (self.real * num2.real + self.img * num2.img) / denom
        img_ = (self.img * num2.real - self.real * num2.img) / denom
        return ComplexNumber(real_, img_)
    
    # Magic method for addition operator (+) overloading
    def __add__(self, num2):
        return self.add(num2)
    
    # Magic method for subtraction operator (-) overloading
    def __sub__(self, num2):
        return self.sub(num2)
    
    # Magic method for multiplication operator (*) overloading
    def __mul__(self, num2):
        return self.mul(num2)
    
    # Magic method for division operator (/) overloading
    def __truediv__(self, num2):
        return self.div(num2)

## Example usage
# Creating two complex numbers and displaying them

num1 = ComplexNumber(1, -2)  # 1 - 2i
print("num1:")
num1.display_number()  # Output: 1 + -2i

num2 = ComplexNumber(-3, -4)  # -3 - 4i
print("num2:")
num2.display_number()  # Output: -3 + -4i

# Performing addition using regular method and displaying result
num3 = num1.add(num2)  # This calls the regular add method
print("num1 + num2 (using add method):")
num3.display_number()  # Output: -2 + -6i

# Using the addition operator (+) which calls __add__ internally
num4 = num1 + num2     # This calls the __add__ magic method (operator overloading)
print("num1 + num2 (using __add__ method):")
num4.display_number()  # Output: -2 + -6i

# Performing subtraction using regular method and displaying result
num5 = num1.sub(num2)  # This calls the regular sub method
print("num1 - num2 (using sub method):")
num5.display_number()  # Output: 4 + 2i

# Using the subtraction operator (-) which calls __sub__ internally
num6 = num1 - num2     # This calls the __sub__ magic method (operator overloading)
print("num1 - num2 (using __sub__ method):")
num6.display_number()  # Output: 4 + 2i

# Performing multiplication using regular method and displaying result
num7 = num1.mul(num2)  # This calls the regular mul method
print("num1 * num2 (using mul method):")
num7.display_number()  # Output: -5 + 10i

# Using the multiplication operator (*) which calls __mul__ internally
num8 = num1 * num2     # This calls the __mul__ magic method (operator overloading)
print("num1 * num2 (using __mul__ method):")
num8.display_number()  # Output: -5 + 10i

# Performing division using regular method and displaying result
num9 = num1.div(num2)  # This calls the regular div method
print("num1 / num2 (using div method):")
num9.display_number()  # Output: 0.44 + 0.08i

# Using the division operator (/) which calls __truediv__ internally
num10 = num1 / num2    # This calls the __truediv__ magic method (operator overloading)
print("num1 / num2 (using __truediv__ method):")
num10.display_number() # Output: 0.44 + 0.08i
