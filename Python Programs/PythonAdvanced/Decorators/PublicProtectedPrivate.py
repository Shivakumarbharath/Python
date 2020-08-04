class Person:
    def __init__(self, name, eno):
        self._name = name  # protected variables cant be used in other files or modules but can be used in same file
        self.__eno = eno  # cant be used outside the class but can be printed

    def display(self):
        print('name-', self._name)
        print('eno-', self.__eno)


o = Person('gtec', 10123)
o._name = 2323
o.eno = 45645
o.display()
print(o._name)
