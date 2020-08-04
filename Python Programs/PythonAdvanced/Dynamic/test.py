import PythonAdvanced.Dynamic.BasicMonkey


def m1(self):
    print('m1 changed')


PythonAdvanced.Dynamic.BasicMonkey.A.m1 = m1
obj = PythonAdvanced.Dynamic.BasicMonkey.A()
obj.m1()
