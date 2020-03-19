#public varibles -has no underscore -can be used anywhere ab=nd can be changed
#protected -has 1 underscore before the variable-asking programmer not to chnage the values
#private - has two underscores - cant change the values outside the class


class Integer(object):#to call and restrict the number of arguments to a particular datatype
    def __init__(self,name):
        self.name=name
        def __get__(self,instance):
            print('get-',instance.__dict__)
            return  instance.__dict__[self.name]
        def __set__(self,instance,val):
            print('set')
            if not isinstance(val,int):
                raise TypeError('Please Enter int value')
            instance.__dict__[self.name]=val
class String(object):
    def __init__(self,name):
        self.name=name
        def __get__(self,instance):
            print('get-',instance.__dict__)
            return  instance.__dict__[self.name]
        def __set__(self,instance,val):
            print('set')
            if not isinstance(val,str):
                raise TypeError('Please Enter int value')
            instance.__dict__[self.name]=val

class Person:
    mobile_no=Integer('mobile_no')
    age=Integer('age')
    name=String('name')
    def __init__(self,name,mobile_no,age):
        self.name=name
        self.mobile_no=mobile_no
        self.age=age

    # mobile_no = String('mobile_no')
    # def mob(self,mobile_no):
    #     self.mobile_no=mobile_no
    # @property
    # def name(self):
    #     return self._name
    # @name.setter
    # def name(self,name):
    #     if not isinstance(name,str):
    #         raise TypeError('invalid name')
    #     self._name=name

obj=Person('gtec',9880361083,25)
print(obj.mobile_no,obj.age,obj.name)
# obj.mob('7259821100')
# print(obj.__dict__)