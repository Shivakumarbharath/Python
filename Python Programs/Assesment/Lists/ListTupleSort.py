'''

 Write a Python program to get a list, sorted in increasing order by the last element in each tuple
 from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

'''
'''
lst1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lst2=[e[1] for e in lst1]
lst2.sort()

lst3=[]
for element in lst2:
    for tuple in lst1:
        if element== tuple[1]:
            lst3.append(tuple)



print(lst3)


'''

# but more efficient Alternative

lst1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(lst1, key=lambda element: element[1]))
print(sorted(lst1, key=lambda element: element[1], reverse=True))

# key will record which par of the list should be sorted
