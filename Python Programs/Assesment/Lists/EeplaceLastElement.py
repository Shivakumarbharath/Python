'''

Write a Python program to replace the last element in a list with another list. Go to the editor
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


'''
import itertools

list1=[1, 3, 5, 7, 9, 10]
list2=[2, 4, 6, 8]
list1.remove(list1[-1])

print((list1+list2))
