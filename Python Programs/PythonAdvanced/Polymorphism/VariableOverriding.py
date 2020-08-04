class Noofpens:
    def m1(*args):
        for i in args:
            print(i)


t1 = Noofpens()
t1.m1(1, 0, 2, 3, 54, 5, 2, 1, 22)


class A:
    t = 10

    def m1(self):
        print('class A m1')


class B(A):
    t = 23

    def m1(self):
        print('class B m1')


t = B()
t.m1()
print(t.t)


class C:
    def bird(self):
        print('swim')


class D:
    def bird(self):
        print('Walk')


class E:
    def bird(self):
        print('Quack')


class duck:
    def code(self, act):
        act.bird()


act = E()
d1 = duck()
d1.code(act)
