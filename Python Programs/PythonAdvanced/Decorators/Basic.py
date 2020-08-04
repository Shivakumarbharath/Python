class Test:
    def __init__(self, a):
        self.a = a

    @classmethod
    def m1(cls):
        print('Class or static', cls)

    @staticmethod
    def m2():
        x = 10
        print('staticmethod')


t = Test(10)
t.m1()
