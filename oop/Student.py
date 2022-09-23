from .Person import Person

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def display_student(self):
        super().display()
        print("Section: ", self.section)
