from array import *

arr=array('i',[])
n=int(input("Enter the length of the array: "))

for i in range(n):
    x=int(input("Enter {} the value".format(i+1)))
    arr.append(x)

print(arr)

#to get the index number of an elelment in array manually

val=int(input("Enter the value for search: "))
k=0
for e in arr:#e for element and i for iterater
    b=False
    if e==val:
        b=True
        print(k)
        break
    k+=1

if b is False:
    print("Element {} not found".format(val))

#Using the inbuilt function

print(arr.index(val))
