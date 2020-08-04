def Add(x, y):
    '''Add function'''
    return x + y


def Sub(x, y):
    '''Subtraction fuction'''
    return x - y


def Mul(x, y):
    ''' Multiply function'''
    return x * y


def Divide(x, y):
    if y == 0:
        raise ZeroDivisionError('Cant divide by zero')
    return x / y
