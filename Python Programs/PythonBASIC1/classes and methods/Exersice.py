class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        ret = str(self.name) + ' is ' + str(self.age) + ' years old.'
        return ret

    def cmpage(self, *args):
        agel = [self.age]
        for arg in args:
            agel.append(arg.age)
        agel.sort()
        print("The oldest dog is %d years old" % agel[len(agel) - 1])


dog1 = Dog('Alexa', 25)
print(dog1)
dog2 = Dog('', 22)
dog3 = Dog("", 90)
dog3.cmpage(dog1, dog2)
