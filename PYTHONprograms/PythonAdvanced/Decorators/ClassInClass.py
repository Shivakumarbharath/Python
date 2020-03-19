class outer:
    def __init__(self):
        print('Outer class obj created')
    class inner:
        def __init__(self):
            print('Inner')
        def m1(self):
            print('ede')
x=outer().inner()

class Test1:
    def mi(self):
        def calc(a,b):
            print('add',a+b)
            print('sub',a-b)
        calc(1,2)
        calc(15,15)
A=Test1()
A.mi()