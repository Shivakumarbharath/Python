import numpy as np

l=[1,2,3]

A=np.array(l)


#for a list
for e in l:
    print(e)

#for an array
for e in A:
    print(e)


#list is appendable
#array is not appendable

#concatination in  list
print(l+[5])

#broadcasting in arrray
#here the number gets added to every element in the list
print(A+[5])


#vector addition is possible in array

print(A+np.array([9,8,7]))


#scalar multiplication in array
print(A*2)

#numpy sqrt
print(np.sqrt(A))
print(A**(0.5))

print(np.sin(A))
