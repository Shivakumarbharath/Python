from array import *
import math

# creating an array

vals = array('i', [5, 2, -6, 3, 8, 7])
val2 = array('u', ['g', 'k', 'l'])
print(vals)

print(val2)

print(vals.buffer_info())

print(vals.typecode)

vals.append(5)
print(vals)

vals.reverse()

print(vals)

# everithing is possible as list
print(list(vals[2:6]))

print(len(vals))

for i in vals:
    print(i)

for i in val2:
    print(i)

print(val2)
# copying an Array

newAray = array(vals.typecode,
                [a ** 2 for a in vals])  # in this method you can perform operations on a and then add to tha new array

newAray2 = array(vals.typecode, vals)  # in this way it is not possible to operate on a and add

print(newAray)
print(newAray2)

# sorting an array

lst = list(newAray)
lst.sort()
newAray = (newAray.typecode, lst)
print(newAray)

# factorial of array
vals.remove(-6)
ArrayFact = array('I', [math.factorial(a) for a in vals])

print(ArrayFact)
