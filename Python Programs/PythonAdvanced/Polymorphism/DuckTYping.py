# polymorphism means multi behaviour
# there are two types 1duck typing and using dependency injection

class Duck:
    def talk(self):
        print("Quack Quack")


class Human:
    def talk(self):
        print("Hello ")


def objtalk(obj):  # the same function works for both the classes with same method thus multiple behaviour
    obj.talk()


d1 = Duck()

h1 = Human()

objtalk(d1)
objtalk(h1)
