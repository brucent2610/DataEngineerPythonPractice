class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

class Tester(Employee):
    def run_tests(self):
        print("Tester is started by {self.name}")
        print("Tester are done")

class Developer(Employee):
    def increase_salary(self, percentage, bonus):
        self.salary += self.salary * ((percentage) / 100)   
        self.salary += bonus    

employee1 = Tester("John", 30, 1200)
employee2 = Developer("Lauren", 44, 1000)

employee1.increase_salary(10)
employee2.increase_salary(20, 500)

print(employee1.salary)
print(employee2.salary)