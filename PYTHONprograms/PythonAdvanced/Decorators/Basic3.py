#decorators are function which takes function and returns a function with performing additional operations
# double decor
def decor(fun):
    def inner():
        result=fun()*2
        return result
    return inner()
def num():
    return 5
res= decor(num)
print(res)

#using @
# @decorater
@decor
def num():
    return 5
