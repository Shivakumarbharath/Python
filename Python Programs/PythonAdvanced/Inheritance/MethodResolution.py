class A:
    def __init__(self):
        print('Aconstrutor')

    def m1(self):
        print(' A m1')


class B:
    def __init__(self):
        print('B construtor')

    def m1(self):
        print(' B m1')

    def m3(self):
        print('m3')


class C(A, B):  # the method of A class will get executed
    def __init__(self):
        print('C construtor')

    def m4(self):
        print('m4')


t = C()
t.m1()
