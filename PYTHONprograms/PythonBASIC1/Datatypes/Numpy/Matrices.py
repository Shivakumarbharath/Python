from numpy import *

arr=array([[1,2,3,8,5,2],
           [2,3,4,2,3,6]
            ])

print(arr)

#dtype gives the type of array
print(arr.dtype)

#ndim gives dimension of array
print(arr.ndim)

#shape gives the (number of rows ,number of columns)
print(arr.shape)

#size gives the number of elements in arrays
print(arr.size)

#converting 2d array to 1d array

arr2=arr.flatten()

print(arr2)


#converting 1d to 2d

arr3=arr2.reshape((3,4))
print(arr3)

#convertng to 3d

arr3=arr2.reshape((2,2,3))
print(arr3)
