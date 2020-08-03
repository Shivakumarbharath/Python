import gc
import sys


class A:
    def __init__(self):
        print('Aconstrutor')

    def m1(self):
        print(' A m1')

    def m5(self):
        print('m5')


class B(A):
    def __init__(self):
        print('B construtor')

    def m1(self):
        print(' B m1')

    def m3(self):
        print('m3')


class C(B):  # the method of B class will get executed if not in B in A will get executed
    def __init__(self):
        print('C construtor')

    def m4(self):
        print('m4')


t = C()
t.m1()
t.m5()
# the number of objects associated with t by using getrefcount
print(sys.getrefcount(t))  # by deafault python will create an object class
t = None  # after the program if none is given to a oobject reference .THe garbage collector clears the memory
print(gc.isenabled())
