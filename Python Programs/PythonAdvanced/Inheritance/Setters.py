# setters and getters can be used instead of construcors
class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setmarks(self, marks):
        self.marks = marks

    def getmarks(self):
        return self.marks


a = Student()
l = []
n = int(input('No of students'))
for i in range(n):
    s = Student()
    name = input('Enter name ')
    marks = int(input('Enter marks'))
    s.name = name
    s.marks = marks
    l.append(s)
    print(s.getName(), s.getmarks())
