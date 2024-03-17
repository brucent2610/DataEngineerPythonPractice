class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"

employee1 = Employee("John", 30, "Software Developer", 1200)
employee2 = Employee("Lauren", 44, "Tester", 1000)

print(employee1.increase_salary(10))
print(employee1.info())

print(employee2.increase_salary(20))
print(employee2.info())


