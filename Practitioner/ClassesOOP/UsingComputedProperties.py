class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
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
    
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 10000:
            raise ValueError("Minmum wage is $1000")   
        self._salary = salary

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        raise AttributeError("Email is read-only")
    
    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @salary.setter
    def password(self, password):
        # Hash password here
        self._password = password

    @property
    def annual_salary(self):
        return self.salary * 12
       
employee1 = Employee("John", 30, "Software Developer", 12000)
employee1.salary = 20000

print(employee1.annual_salary)




