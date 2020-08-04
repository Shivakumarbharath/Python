class A:
    def __init__(self, carno, carname):
        self.carno = carno
        self.carname = carname
        print('Aconstrutor')

    def m1(self):
        print('m1')


class B(A):
    def __init__(self, eno, ename, carno, carname):
        super().__init__(carno, carname)  # to inherit the parent class constructor
        self.eno = eno
        self.ename = ename
        print('B', self.eno, self.ename, self.carname, self.carno)

    def m2(self):
        print('m2')
    # can call also like A.m3(0) but it must have an argument


class C(A):
    def __init__(self):
        print('C construtor')


t = B(2, 'bharath', 2121, 'benz')
t.m1()
t.m2()
t1 = C()
t1.m1()
