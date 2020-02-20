class Test:
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
        Test.a=111
    def m1(self):
        print(self.a)
        print(Test.a)
        Test.a=222#class level gets modified and wherever a is used 222 will be printed
        self.a=333#only object level is changed
        print(self.a)
    @classmethod
    def m2(cls):
        print(cls.a)#Take  Reference
        print(Test.a)#Take class Reference
        cls.a=444
        print(cls.a)
    @staticmethod
    def m3():
        Test.a=555
        print(Test.a)
a=Test()
a.m1()
a.m2()
a.m3()
