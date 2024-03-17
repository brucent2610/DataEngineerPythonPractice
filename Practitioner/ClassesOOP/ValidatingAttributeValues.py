class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"
    
    def __repr__(self):
        return (
            f"Employee( "
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        ) 
    
    def get_salary(self):
        # return f"${self.salary}"
        # return round(self.salary, 2)
        return self.salary

    def set_salary(self, salary):
        if salary < 10000:
            raise ValueError("Minmum wage is $1000")   
        self.salary = salary
       
employee1 = Employee("John", 30, "Software Developer", 1200)
employee1.set_salary(500)
print(employee1.get_salary())   # ValueError: Minmum wage is $1000




