class student:
    def getstudent(self):
        self.name=input('Enter your Name: ')
        self.age=input('Age: ')
    def __str__(self):
        return (str(self.name)+'\n'+str(self.age))
stu=student()
stu.getstudent()
print(stu)