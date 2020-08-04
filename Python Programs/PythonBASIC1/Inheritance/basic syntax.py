# syntax is to add a another class name in a new class in paranthesis
# Inheritance allows us to define a class that inheritence
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname + ' ' + self.lastname)


# inherited class
class Student(Person):
    def __init__(self, firstname, lastname, standard):
        Person.__init__(self, firstname, lastname)
        self.standard = standard

    def printname(self):
        print("Welcome " + self.firstname + ' ' + self.lastname + ' to ' + self.standard)


student = Student('Eddy', 'Alvaris', '5')
student.printname()
# to check the clas of the object
print(isinstance(student, Person))
# issubclasss to check
# multiple Inheretence
