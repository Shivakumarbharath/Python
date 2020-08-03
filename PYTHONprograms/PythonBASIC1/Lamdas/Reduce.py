from functools import reduce

lst = [5, 10, 25, 12, 12, 15]
result = reduce(lambda x, y: x + y, lst)
print(result)
