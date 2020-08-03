class Student:
    def __init__(self):
        self.__name = "John"  # to make them private# that is it cannot be accesed outside the class in any object
        self.__id = 15326

    def DisplayP(self):
        print(self.__id)
        print(self.__name)


s1 = Student()
# print (s1.__id) this cannoot be used as the id is private if you want to print use the display method

s1.DisplayP()

# print(s1._Student.__id);   given but not working
