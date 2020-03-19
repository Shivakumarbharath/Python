class Person:
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile

    @property
    def name(self):
        return self._name


    @name.setter#this is encapsulation i.e. assining the datatype to arguments
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError('invalid name')
        self._name=name
    def __getattr__(self, name):
        return "invalid value ={}".format(name)
    def __setattr__(self, name, value):
        if name not in {'name','mobile'}:
            raise TypeError('Invalid Attribute')
        self.__dict__[name]=value

o=Person('gtec',987654)
print(o.mobile)