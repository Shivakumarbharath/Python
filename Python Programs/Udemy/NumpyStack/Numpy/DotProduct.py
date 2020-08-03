import numpy as np

# dot product with numpy

a = np.array([1, 2])
b = np.array([3, 4])

m = a * b
# multiply each element


'''
for e in m:
    dot+=e
'''

dot = np.sum(m)
print(dot, ' ', np.dot(a, b))

'''
(a*b).sum()
np.sum(a*b)


gives the same result

can use the dot inbuilt function like 
a.dot(b)


can use the symbol @


'''

print(a @ b)

'''
we know that 

a.b=abcos@

'''
# to get magnitude of a
amag = np.sqrt((a * a).sum())

print(amag)

# to get magnitude of b
bmag = np.sqrt((b * b).sum())

print(bmag)

# To do this we can use linear algebra class of numpy

amag1 = np.linalg.norm(a)  # this gives the magnitude of a

print(amag1)

# similarly
bmag1 = np.linalg.norm(b)
print(bmag1)

# to find the cosine of th eangle
cosangle = a.dot(b) / (amag1 * bmag1)

print(cosangle)

# to get the angle

angle = np.arccos(cosangle)  # this is inverse of cosine

# Angle in radians
print(angle)
