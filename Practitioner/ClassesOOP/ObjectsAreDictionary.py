class Employee:
    def __init__(self):
        self.name = "John"
        self.age = 30   
        self.position = "Software Developer"
        self.salary = 1200

e = Employee()

# Print Object Employee allocate in memory
print(e)

# Print to Dict
print(e.__dict__)

# Print to Class
print(e.__class__)

# Class Functions for Constructing an Object
# __new__: Allocate memory for the new object and send it to the __init__ function
# __init__: Receive a new object from __new__ function as a "self" parameter

