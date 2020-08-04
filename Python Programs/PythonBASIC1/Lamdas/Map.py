# map taks a lambda expression
# using a map we can manipulate the values in a list and store it in another list
lst = [1, 5, 9, 7, 9, 5, 63, 2, 5, 7, 8, 6, 5, 6, 8, 8, 8, ]
result = map(lambda n: n * 2, lst)  # we have to type cast it
print(result)
result = list(map(lambda n: n * 2, lst))
print(result)
