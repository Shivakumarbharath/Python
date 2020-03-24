from numpy import *

'''
There are 6 ways of creating an array

1. array() 
2.linespace()
3.logspace()
4.arange()
5.zeros()
6.ones()

'''
# Using array(list,TypeOPtional)
arr=array([1,2,3,4,5,6])
# here the data type is optional and syntax has a small change arr=array([1,2,3,4,5,6],int)
#even if float is given and specified as in t it will convert the array into int
print(arr)

#to check the type
print(arr.dtype)


#using linespace(start ,stop ,divideIntoParts)
ls=linspace(0,9,15)
#it means the numbers 0-9 is divided into 15 parts and returnd
#default i,e., not providing parts takes as 50 part
#stop number included
print(ls)



#using arange(start,stop,steps)
arg=arange(0,15,2)# it is a-range rather than arrange
#it means numbers from 0-15 skipping (steps-1) numbers in between
#stop number not included
print(arg)

#using logspace(start,stop,divide) all interns of log

losA=logspace(1,3,3)
#Returns from log(start) to log(stop) divided into parts logarithmically by divide
print(losA)
print('%.2f'%losA[2])


#Using zeros(size,type)
zs=zeros(5,int)
print(zs)

#Using ones(size,type)
os=ones(5,int)
print(os)


