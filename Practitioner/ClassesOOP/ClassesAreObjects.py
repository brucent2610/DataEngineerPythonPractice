class Employee:

    # One purpose of using class attributes is to store the value which is constant for all instances of the class
    # Instance of class is an object of the class that is created using the class constructor  
    min_wa = 1000

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.min_wa:
            raise ValueError("Minmum wage is $1000")   
        self._salary = salary

print(Employee.__dict__)
