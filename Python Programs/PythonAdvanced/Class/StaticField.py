class Student:
    major="ECE"# this variable is known as static field which is constant for all objects


    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum


s1=Student("Bharath",2121)
s2=Student("Shrey",2133)
print(s1.rollnum,s1.name,s1.major)
print(s2.rollnum,s2.name,s2.major)


