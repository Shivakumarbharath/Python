'''

Find the second smallest number in a list

'''

lst = [1, 2, -8, -2, 0, -2, -2, -2]
set1 = set(lst)
lst = list(set1)
lst.sort()
print(lst[1])
