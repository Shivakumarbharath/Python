'''

 Write a Python program to get the difference between the two lists.

'''

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [6, 7, 8, 9, 10]

# for x in lst2:
#     lst1.remove(x)

# print(lst1)


print(list(set(lst1) - set(lst2)))
