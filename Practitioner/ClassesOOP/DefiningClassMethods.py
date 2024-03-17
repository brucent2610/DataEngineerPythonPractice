from datetime import date

class Employee:

    min_wa = 1000

    # Classmethod that wil change the value of the class attribute min_wa
    @classmethod
    def changing_min_wage(cls, amount):
        if amount > 1000:
            raise ValueError("Company is bankrupt")
        cls.min_wa = amount

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.min_wa)

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

e = Employee.new_employee("John", date(1990, 1, 1)) 
e2 = Employee.new_employee("John 2", date(1990, 1, 1)) 
print(e.name)
print(e.age)
print(e.salary)
Employee.changing_min_wage(500)
print(Employee.min_wa)
print(e.min_wa)
print(e2.min_wa)
