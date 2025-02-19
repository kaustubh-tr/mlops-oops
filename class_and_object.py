# Initiate a class
# class name casing generally follows CamelCasing

class Employee:
    # Magic method or dunder method
    # Constructor
    def __init__(self, employee_id, salary, designation):
        print("Initializing employee attributes...")
        # Attributes
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

# Creating an instance (object) of the Employee class
employee1 = Employee(
    employee_id=101,
    salary=10_00_00,
    designation="Data Scientist"
)
print(type(employee1))  # Display the type of object (Employee)

# Call the methods on the employee object
print()
employee1.project("Project1")
employee1.travel("City1", "Project2")

## function vs method
# A function is a block of code that performs a specific task and can be defined outside of a class.
# A method is essentially a function that is defined inside a class.
