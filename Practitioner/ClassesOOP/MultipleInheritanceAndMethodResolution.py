class Employee:

    __slots__ = ('name', 'age', 'salary')

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

    __slots__ = ('framework',)


    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework


    def increase_salary(self, percentage, bonus):
        super().increase_salary(percentage)
        self.salary += bonus    

employee1 = Tester("John", 30, 1200)
employee2 = Developer("Lauren", 44, 1000, "Flask")