# A method is a class-specific function, that relates to the class. It includes self as the first parameter.
# Doesn't need to return anything, but the function should be related to the class.


class Person:  # Class keyword creates a class.
    def __init__(self, name, age):  # Name and age are parameters. Init stands for initialize, and constructs the
        # person. self. can be anything
        self.name = name
        self.age = age
        print(self.isminor())  # New addition

    def isminor(self):
        if self.age <= 18:
            return True
        else:
            return False


new_person = Person("Sam Smith", 32)  # Prints false with new addition
print(new_person.isminor())  # Prints false.

class Classroom:
    def __init__(self, numberOfStudents, numberOfDesks, course):
        self.numberOfStudents = numberOfStudents
        self.numberOfDesks = numberOfDesks
        self.course = course

    def __len__(self):
        return self.numberOfStudents

    def __str__(self):
        return "There are " + str(self.numberOfDesks) + " students in " + str(self.course) + ".\nThere are " +\
               str(self.numberOfStudents) + " in the course."


room205 = Classroom(16, 20, "Grade 12 Computer Science")
print(room205)  # Prints the str dunder method section.
print(len(room205))  # Shows the class length, which is the number of students.





