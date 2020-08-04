class A:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    @property
    def name(self):
        return self._name

    @property
    def mobile(self):
        return self._mobile

    @name.setter  # this is encapsulation i.e. assining the datatype to arguments
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('invalid name')
        self._name = name

    @mobile.setter
    def mobile(self, mobile):
        if not isinstance(mobile, int):
            raise TypeError('invalid number')
        self._mobile = mobile


obj = A('khbdc', 987654321)
print(obj.__dict__)
