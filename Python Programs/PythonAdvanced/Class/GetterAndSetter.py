class Programmer:
    # def __init__(self,name,salary,technolgies):
    #     self.name=name
    #     self.salary=salary
    #     self.technolgies=technolgies
    def setName(self, n):  # it is  the mutator method
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTecnologies(self, technology):
        self.technology = technology

    def getTecnologies(self):
        return self.technology


p1 = Programmer()
p1.setName("John")
p1.setSalary(50000)
p1.setTecnologies("Python")

print(p1.getName())
print(p1.getSalary())
print(p1.getTecnologies())
