# Initiate a class
# class name casing generally follows CamelCasing

class Employee:
    # Magic method or dunder method: These are methods that have double underscores at the beginning and end
    ## Constructor: only __init__() method is a constructor and is automatically called when a new object of the class is created

    # Class Attributes (also static variable)
    company_name = "ABC"
    # name = "anonymous"
    
    # Default constructor: This is a constructor that doesn't take any parameters
    def __init__(self):
        pass

    # Parameterised constructor + Default constructor (because of None)
    def __init__(self, name="anonymous", employee_id=None, salary=None, designation=None):
        print("Initializing employee attributes...")
        # Object Attributes (these are specific to each instance)
        
        # Precedence of Object Attribute > Class Attribute
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.designation = designation
        print("Employee attributes initialization done!")

    # Method-1
    def project(self, title):
        print(f"Employee with ID {self.employee_id}, Designation: {self.designation}, is assigned to project '{title}'.")

    # Method-2
    def travel(self, destination, title):
        print(f"Employee with ID {self.employee_id}, Designation: {self.designation}, is travelling to {destination} for '{title}' related work.")

# Creating an instance (object) of the Employee class using parameterized constructor
employee1 = Employee(
    name="John Doe",
    employee_id=101,
    salary=10_00_00,
    designation="Data Scientist"
)
print(type(employee1))  # Display the type of object (Employee)

# Creating an instance (object) of the Employee class using default constructor
employee2 = Employee()
print(type(employee2))  # Display the type of object (Employee)

# Call the methods on the employee1 object
print()
employee1.project("Project1")
employee1.travel("City1", "Project2")

# Call the methods on the employee2 object (created using the default constructor)
print()
employee2.project("Project3")
employee2.travel("City2", "Project4")

# del keyword: used to delete objects, variables, or attributes
print()
del employee1.salary  # Deletes the 'salary' attribute from employee1 object
print("After deleting salary:", hasattr(employee1, 'salary'))  # Should print False

del employee1  # Deletes the 'employee1' object
# print(employee1)  # Uncommenting this line would raise an error as the object is deleted.


## function vs method
# A function is a block of code that performs a specific task and can be defined outside of a class.
# A method is essentially a function that is defined inside a class.

## what is self?
# self refers to the current instance (object) of the class.
# It is automatically passed to instance methods, allowing access to the object's attributes and methods.


## Class Attribute vs. Instance (Object) Attribute
# 1. Instance Attribute:
#    - Unique to each object. These values can differ between instances.
#    - Example: `name`, `employee_id`, `salary`, and `designation` in the `Employee` class.

# 2. Class Attribute:
#    - Shared across all instances of the class. It doesn't change for each object.
#    - Example: `company_name` in the `Employee` class.

# A class consists of two main components:
# 1. Attributes (data) -> Properties that store information (e.g., `name`, `salary`).
# 2. Methods -> Functions defined within the class that operate on the data (e.g., `project()`, `travel()`).
