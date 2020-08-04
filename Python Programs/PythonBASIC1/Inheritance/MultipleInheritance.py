# parent 1class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Printperson(self):
        print(self.name + '  ' + str(self.id))


# parent2 class
class Employee:
    def __init__(self, salary, post):
        self.salary = salary
        self.post = post

    def Printemplyee(self):
        print(str(self.salary) + '  ' + str(self.post))


class Leader(Person, Employee):
    def __init__(self, name, id, salary, post, points):
        Person.__init__(self, name, id)
        Employee.__init__(self, salary, post)
        self.points = points

    def Printperson(self):
        Person.Printperson(self)
        Employee.Printemplyee(self)

    def __str__(self):
        return (str(self.name) + '\n' + str(self.id) + '\n' + str(self.post))


manager = Leader('Tom', 45525, 40000, 'manager', 25000)
manager.Printperson()
