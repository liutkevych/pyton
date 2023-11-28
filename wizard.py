class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    ...

student = Student("Daryna", "Krakow")
professor = Professor("Alex", "Engineering management")

print(student.name)
print(professor.name, professor.subject)