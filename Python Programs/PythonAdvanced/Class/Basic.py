'''
VARIABLES IN CLASS
1.Instant Variables- Object
2.Static Variables-Class
3.Local Variables- Method Level -instance level
Priority Order is As Above
 '''

# CONSTRUCTOR
'''
if there is Two init(constructor) the latest will be executed 
'''


class Student:
    '''This is Student Class'''

    def __init__(self, empno, empname, std):  # Executes only once While creating the object
        self.id = empno
        self.name = empname
        self.std = std
        # print('Constructor')

    def m1(self):  # Executes according to requirment
        print('Roll NU0M =', self.id)

    def m2(self):
        pass


a = Student(2, 't', 5)
a.age = 66  # can create instant Variable outside the Class only for That Object
print(a.__dict__)
a.name = 'mmmmmmmm'
print(a.__dict__)
b = Student(454, 'Tom Cruise', 12)
print(b.__dict__)
print(a.__doc__)  # to print the comment statments
# deletion is possible only for object level and not class level
# To change the class level variables class.variable
# But self.variable does not get changed
