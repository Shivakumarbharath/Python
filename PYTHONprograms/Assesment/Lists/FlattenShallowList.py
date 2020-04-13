'''
Flatten a shallow list
'''
import itertools


lst1=[[1,2,3],[4,5],[78,9]]

lst2=[7,8,5,6,3,2]

#2 ways
print(list(itertools.accumulate(lst2)))#p0, p0+p1, p0+p1+p2, …




print(list(itertools.chain(lst1)))



print(list(itertools.chain.from_iterable(lst1)))
