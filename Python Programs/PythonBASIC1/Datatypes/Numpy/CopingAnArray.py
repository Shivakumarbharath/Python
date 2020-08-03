from numpy import *

arr=array([1,2,3,4,5,6,7,8,9,0])

#To add a number to every element in array

arr2=arr+5

print(arr2)

#elements inside the arrays are added
arr3=arr+arr2

print(arr3)
arr4=list(arr)

print(arr4)


arr5=array(arr4)

print(arr5)


#sum off array

print(sum(arr))
#sin or cos of arrayor any math funtions


print(sin(arr))
print(sqrt(arr5))

#can use max or min in an array and many more

#sorting
print(sort(arr3))


#concatinate 2 arrays

p=concatenate([arr,arr3])#take care of syntax

print(p)

#to copy it is better to clone because both the arrays will point on same address
#check

arr6=arr

print(id(arr))#id gives the address of the variable
print(id(arr6))
#both are same so we need to clone  it
#cloning and this is shallow copy and changes are dependent on each other
# that is change in one array changes the array

#shallow Copy
arr6=arr.view()#will help to create an new array I.E to make two different adress locations

print(id(arr))#id gives the address of the variable
print(id(arr6))


#deep copy-change in one array does not effect change in other array

arr6=arr.copy()