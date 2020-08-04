'''

Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']

'''

colour1 = ["red", "orange", "green", "blue", "white"]
colour2 = ["black", "yellow", "green", "blue"]
colour1_set = set(colour1)
colour2_set = set(colour2)

print(list(colour1_set.difference(colour2_set)))

print(list(colour2_set.difference(colour1_set)))

'''

Write a Python program to find a tuple, the smallest second index value from a list of tuples.

'''

lst = [(4, 1), (1, 2), (6, 0)]

print(min(lst, key=lambda x: x[1]))

'''

Print a list of space-separated elements

'''

import array

num = [1, 2, 3, 4, 5]

print(*num)
