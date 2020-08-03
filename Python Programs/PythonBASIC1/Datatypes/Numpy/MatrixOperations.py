from numpy import *

arr = array([[1, 2, 3],
             [2, 3, 4],
             [5, 3, 2]
             ])

b = matrix(arr)

c = matrix('2 3 6 ; 5  5 9 ; 10 4 7')

# print(b)

# print(c)

# to get diagonal elements
print(diagonal(c))

# to get minimam and max element

print(c.min())
print(c.max())

# matrix addition
m3 = b + c
print(m3)

# matrix multiplication
m3 = b * c
print(m3)
