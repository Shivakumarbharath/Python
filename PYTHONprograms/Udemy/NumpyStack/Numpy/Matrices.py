import numpy as np

a= np.array([[1,2],[3,4]])

print(a)#it prints as a matrix which is not the case in the list

#the elements can be accesed as
print(a[0,1])

#to access the row
print(a[0],' Row')

#To print a column

print(a[:,0],' Column')
#it returns column at index 0
#here :means everything in this dimension ,0 is columns as 0, are for rows

#To find the transpose of the matrix

print(a.T,' transpose')

#Matrix multipliacation

#2x3 matrix

#be cautius about th edimentions

b=np.array([[2,3,5],[7,8,9]])
print(b)

#it is done by dot product

print(a.dot(b),' multiplication')

#determinant
det=np.linalg.det(a)

print(det,' deteminant of a')

#inverse of a
inv=np.linalg.inv(a)

print(inv,' inverse of a')
#checking the inverse

#a*inv(a)=diagonal matrix

print(a.dot(inv), ' inverse check')

#traces
print(a.trace(), ' trace')

#diagonal function

print(np.diag(a),' digonal of a')
#here the matrix is converted into vector

print(np.diag([1,4]))
#here the vector is converted into matrix

#Eigen values and eigen vectors

print(np.linalg.eig(a),' eigen values and eigen vctors')
#fist array is the eigan values and the second array is eigen vector

#can be assigen to two variables
lam,v=np.linalg.eig(a)

print(lam,' eigen values')

print(v,' eigen vectors')


#comparing numpy arrays
#here to check the eigen values

print(np.allclose(v[:,0]*lam[0],a @ v[:,0]), ' array comparision')

#to check all the eigen vectors at the same time

print(np.allclose(v@np.diag(lam),a@v))


#if the matrix is symmetric use np.linalg.eigh()