# Task 1: Create a class called School with 3 different attributes. Instantiate an object of that class and print a
# sentence where you had to access the attributes.


class School:
    def __init__(self, city, province, students):
        self.city = city
        self.province = province
        self.students = students


new_school = School("Toronto", "Ontario", 400)
print("The school is in the city " + str(new_school.city) + ".\nThe school is in the province " +
      str(new_school.province) + ".\nThe school has " + str(new_school.students) + " students.\n\n")

# Create a class called Car with however many attributes you feel are appropriate (but one must be numberOfDoors).
# After you assign your attributes, use your numberOfDoors attribute to assign a new attribute the value of “coupe”
# (2-door) or “sedan” (4-door). Access your new attribute and print it to the console.


class Car:
    def __init__(self, numberOfDoors, colour, brand):
        self.colour = colour
        self.brand = brand
        self.numberOfDoors = numberOfDoors
        if self.numberOfDoors == 2:
            self.numberOfDoors = "Coupe"
        elif self.numberOfDoors == 4:
            self.numberOfDoors = "Sedan"

new_car = Car(4, "Red", "Toyota")
print("This car is a " + new_car.numberOfDoors + ".\nIt is " + new_car.colour + "\nIt is made by "
                                                                                "" + new_car.brand + ".\n\n")
new_car = Car(2, "Blue", "Ford")
print("This car is a " + new_car.numberOfDoors + ".\nIt is " + new_car.colour + "\nIt is made by "
                                                                               "" + new_car.brand + ".\n\n")

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

print(MyClass.classmethod())
