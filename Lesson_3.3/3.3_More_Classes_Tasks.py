# Create a class for Universities. It will be instantiated with the attributes: schoolName, numberOfStudents,
# address, and mascot
# Create a class called Program that holds attributes for university programs. It will be instantiated with the
# attributes: programName, faculty, and maxStudents
# Create a class called Student that is instantiated with the attributes: name, birthYear, and originCity
# Create a method for the University class called addProgram(program) that appends the program parameter (an object of
# the Program class) to a list attribute of programs
# Create a method for the Program class called addStudent(student) that appends the student parameter to a list
# attribute of students
# Create 1 School object, 2 Program objects and, 4 student objects. Add 2 students to each program and both programs to
# the school.
# Print every student in the school on their own line like "Jane Doe is in Forensic Science at Dalhousie"
# by using the dunder str function for School


class Student:
    def __init__(self, name, birthYear, originCity):
        self.name = name
        self.birthYear = birthYear
        self.originCity = originCity


class Universities:
    def __init__(self, schoolName, numberOfStudents, address, mascot):
        self.schoolName = schoolName
        self.numberOfstudents = numberOfStudents
        self.address = address
        self.mascot = mascot
        self.program_list = []  # Does not need to be in the parameter, no data passed.

    def addProgram(self, program):
        self.program_list.append(program)

    def __str__(self):  # HERE
        holder = ""
        for program in self.program_list:
            for student in program.student_list:
                holder += student.name + " is in " + program.programName + " is at " + self.schoolName + "\n"
        return holder

class Program:
    def __init__(self, programName, faculty, maxStudents):
        self.programName = programName
        self.faculty = faculty
        self.maxStudents = maxStudents
        self.student_list = []

    def addStudent(self, student):
        self.student_list.append(student)


def variable_defining():
    university = Universities("UBC", 55000, "2329 West Mall, Vancouver", "Thunderbird")
    commerce = Program("Commerce", "Sauder School of Business", 4000)
    compsci = Program("Computer Science", "Department of Computer Science", 1840)
    leo = Student("Leo Sandler", 2002, "Toronto")
    bill = Student("Bill Gates", 1955, "Seattle")
    warren = Student("Warren Buffett", 1930, "Omaha")
    elon = Student("Elon Musk", 1971, "Pretoria")
    commerce.addStudent(warren)
    commerce.addStudent(elon)
    compsci.addStudent(bill)
    compsci.addStudent(leo)
    university.addProgram(commerce)
    university.addProgram(compsci)
    print(str(university))


variable_defining()
