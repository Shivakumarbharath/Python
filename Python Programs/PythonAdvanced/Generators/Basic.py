# normal program
# def square(num ):
#     result=[]
#     for i in num:
#         result.append(i**2)
#
#     return result
# this returns a list
#

# using generators
def square(num):
    for i in num:
        yield i ** 2


result = square([1, 2, 3, 4])

print(next(result))
print(next(result))
print(next(result))
print(next(result))

# we can use for loop

# advantage
# generators does not hold all the values at a time in memory
# if millions of iterations are there then using generators memory can be managed
# it is also good in the time complexity

# it waits untill someone is asking for the values
