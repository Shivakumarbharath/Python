# Eexplicitly -Outside class
# IMplicitly=inside class
class Test:
    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c
        # do not call other methods in constructor(not a good practice)

    def m1(self):
        x = 100  # can be used only inside this method and cannot be changed explicitly
        Test.a = 222
        self.a = 5555
        self.m2()  # to call other methods in required methods

    def m2(self):
        print(self.c)


t = Test(1, 2, 3)
t.m1()
print(t.__dict__)
# instance method means the variables in init can be accessed in other methods by passing self in that particular method
