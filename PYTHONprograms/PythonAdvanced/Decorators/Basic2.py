from functools import wraps
def log(funct):
    @wraps(funct)
    def wrapper(n1,n2):
        n1+=1
        n2+=1
        print('calling'+funct.__name__)
        print('to'+funct.__name__)
        return  funct(n1,n2)
    return wrapper

@log
#add=log(add)
def add(n1,n2):
    '''
    adding
    '''
    print(n1+n2)

@log
def sub(n1,n2):
    print(n1-n2)

@log
def mul(n1,n2):
    print(n1*n2)

@log
def div(n1,n2):
    print(n1/n2)

add(1,2)
help(add)