# An object is a data with a type.
# Instantiating is making an instance of a new object.
empty_dict = {}  # Creating an instance/not creating. Calling upon the blueprints
# All data types have templates. An object is created from a data type. The data type is the blueprint.
# Classes are our own data types. Class names have a capital letter. Classes can be inside of classes.


class Person:  # Class keyword creates a class.
    def __init__(self, name, age):  # Name and age are parameters. Init stands for initialize, and constructs the
        # person. self. can be anything
        self.name = name
        self.age = age


new_person = Person("Leo Sandler", 16)
print(new_person.age)  # Self is the instance, and the instance is new person.


class Classroom:
    def __init__(self, numberOfStudents, numberOfDesks, course):
        self.numberOfStudents = numberOfStudents
        self.numberOfDesks = numberOfDesks
        self.course = course


room205 = Classroom(16, 20, "ICS4U")
room211 = Classroom(19, 19, "ICS3U")

if room211.course != room205.course:
    print("These aren't the same course!")