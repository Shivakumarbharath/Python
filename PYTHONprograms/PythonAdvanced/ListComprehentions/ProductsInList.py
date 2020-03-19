lst=[8,6,7,5,9,4,2,1,8,6,2,1]
lst=[lst[x]*lst[(x+1)] for x in range(0,11)]
print(lst)
a=[2,6,5,8]
b=[3,9,5,8]
c=[a[x]*b[x] for x in range(len(a))]
print(c)