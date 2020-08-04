# decorators are function which takes function and returns a function with performing additional operations
# double decor
import time


def decor(fun):
    def inner():
        t1 = time.time()
        result = fun()
        t2 = time.time()
        print(t2 - t1)
        return result

    return inner()


# def num():
#     return 5
# res= decor(num)
# print(res)

# using @
# @decorater

@decor
def num():
    return 5


@decor
def num2():
    return 100


print(num)

print(num2)
