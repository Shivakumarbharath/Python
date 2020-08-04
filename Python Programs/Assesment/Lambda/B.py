'''

 Write a Python program to square and cube every number in a given list of integers using Lambda.

'''
lst = [2, 3, 4, 5, 6]
print('Original list of integers:\n', lst)
print('Square every number of the said list:\n', list(map(lambda x: x ** 2, lst)))
print('Cube every number of the said list:\n', list(map(lambda x: x ** 3, lst)))
