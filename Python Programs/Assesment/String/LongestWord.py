'''
Write a Python function that takes a list of words and returns the length of the longest one.

["PHP", "Exercises", "Backend"]
'''

lst = ["PHP", "Exercises", "Backend"]
# or
# lst=input("Enter the words).split(',')
print(max(list(map(len, lst))))
print(max(lst, key=len))
