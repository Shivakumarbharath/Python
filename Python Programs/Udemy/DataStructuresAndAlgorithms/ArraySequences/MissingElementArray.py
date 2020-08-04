'''

Given an array 1 and another array 2 is copy of shuffeled
array 1 and removal of any random element

Find the missing element in arrray two

Algorithm
1.Sort both lists
2.Check each element if equal
3.IF not equal that is the missing element


'''

import random

arr1 = [1, 2, 3, 4, 9, 5, 8, 6, 5, 8, 7, 4]
arr2 = arr1[:]
random.shuffle(arr2)
k = arr2.pop(random.choice(arr2))
print(k)
arr1.sort()
arr2.sort()
print(arr1)
print(arr2)
print(list(zip(arr1, arr2)))


def missing_num(arr1, arr2):
    for a, b in zip(arr1, arr2):
        if a != b:
            return a

    return arr1[-1]


print(missing_num(arr1, arr2))
