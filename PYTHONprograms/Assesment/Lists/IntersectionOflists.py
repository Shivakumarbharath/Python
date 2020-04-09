'''

 Write a Python function that takes two lists and returns True if they have at least one common member

'''

lst=[5,6,5,8,9,3,2,7,4,1,5,6,9,8]
lst2=[5,2,3,1,00,2,3,6,5,8,77,8,5,6,85]
lst3=[0,0,0,0,0,0,0]

def Equal(lst,lst2):
    res=False
    for l1 in lst:
        for l2 in lst2:
            if l1 == l2:
                res=True

    return res




print(Equal(lst,lst2))
print(Equal(lst,lst3))
print(Equal(lst3,lst2))
