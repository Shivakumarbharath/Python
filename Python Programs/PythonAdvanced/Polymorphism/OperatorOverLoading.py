class Noofpens:
    def __init__(self,pens):
        self.pens=pens
    def __add__(self, other):
        return (other.pens+self.pens)
    def __mul__(self, other):
        return (other.pens*self.pens)
    def __sub__(self, other):
        return (other.pens - self.pens)
    def m1(self,*args):#last and latest method
        print(len(args))
s1=Noofpens(100)
s2=Noofpens(20)
print(s1+s2)
print(s1*s2)
print(s2-s1)
s1.m1(1,2,3,4,5,6,7,8,9,10)
'''
+   __add__
-   __sub__
*   __mul__
/   __div__
>   __gt__
<   __lt__
==  __eq__
+=  __iadd__
-=  __isub__
*=  __imul__
/=  __idiv__
>=  __ge__
<=  __le__
'''