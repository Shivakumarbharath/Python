from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('logged',func.__name__,args[1:],kwargs)
        return func(*args,**kwargs)
    return wrapper

def logmethod(cls):
    for key,value in list(vars(cls).items()):
        if callable(value):
            setattr(cls,key,logged(value))
    return cls

@logmethod
class Ex:
    g=1000
    def spam(self,n1,n2):
        print('spam',n1,n2)
    def yellow(self,a):
        print('yellow')

o=Ex()
o.spam(100,200)
