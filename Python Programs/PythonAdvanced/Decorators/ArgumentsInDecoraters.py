from functools import wraps
def log_wa(fmt):
    def log(funct):
        @wraps(funct)
        def wrapper(n1,n2):
            n1+=1
            n2+=1
            print('calling'+funct.__name__)
            print(fmt,'to'+funct.__name__)
            return  funct(n1,n2)
        return wrapper
    return log

@log_wa('add:')
#add=log(add)
def add(n1,n2):
    '''
    adding
    '''
    print(n1+n2)

@log_wa('differ')
def sub(n1,n2):
    print(n1-n2)

@log_wa('product')
def mul(n1,n2):
    print(n1*n2)

@log_wa('quotient')
def div(n1,n2):
    print(n1/n2)

add(1,2)
print(sub(23,12))