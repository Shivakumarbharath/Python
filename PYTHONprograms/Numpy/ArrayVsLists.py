import numpy as np

l=[1,2,3]

a=np.array(l)

for e in a:
    print(e)

l.append(4)
#size of list is not fixed
#size of array is fixed

'''
SimmilaritiesL:
1.Both are useds to store data
2.Both are mutable
3.Can be indexed
4.Both can be sliced

Differences
1.List can store all types of data
arrays can store only one type of data

2.In arrays different operations can be performed not possible in list

List concatination is possible 
But this is not possible in array


Advantages of Array

1.Less Memory
2.Speed
3.convienent to use



'''