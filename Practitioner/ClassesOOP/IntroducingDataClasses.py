from dataclasses import dataclass

@dataclass
class Project:
    name: str
    payment: int
    client: str

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary   
        self.project = project

p = Project("Project1", 1000, "Client1")
e = Employee("John", 30, 1200, p)
print(e.project)