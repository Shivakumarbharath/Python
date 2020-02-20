'''
class A:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
    def m1(self):
        if self.eno== 0:
            raise TypeError('Please Enter the valid Number')
        return self.eno
o=A(100,'haha')
print(o.m1())
'''
class Numbervalid(Exception):
    def __str__(self):
        return 'Please enter values above 100'
#we can use whenever we do not want to end the program due an error
try:
    n1=input('Enter n1')
    n2=input('Enter n2')
    if int(n1)<100 or int(n2)<100:
        raise Numbervalid(n1,n2)#jumps to to line 25
    print((int(n1)+int(n2)))
except(ValueError,TypeError):
    print('Please n1 and n2 as integers')
except Numbervalid as e:
    print(e,e.args)

except:
    print('PLease Enter Numeric Arguments only')
finally:
    print("End Of Program")