class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

employee1 = Employee("John", 30, "Software Developer", 1200)
employee2 = Employee("Lauren", 44, "Tester", 1000)

print(employee1.name)
print(employee2.name)

