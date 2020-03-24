'''
1. Create an array of 5 elements and delete the element at index 2 and then print.

2.Write a code to reverse the value without using inbuilt function
'''
from  array import *
#1
x=input("Enter 5 numbers seperated by comma : ").split(',')
y=[]
for e in x:
  e=int(e)
  y.append(e)
val=array('i',y)
for i in range(5):
    if i ==2:
        val.remove(val[i])

print(val)

#2

a=list(val)
a=a[::-1]
val=(val.typecode,a)
print(val)