'''

 Write a Python program to find the list in a list of lists whose sum of elements is the highest. Go to the editor
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]

'''

a=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

print(max(a,key=sum))


'''

Write a Python program to find all the values in a list are greater than a specified number

'''

n=3

lst=[1,2,3,4,5,6,10,11,12,23]


print(list(map(lambda x: x if x >n  else lst.remove(x) , lst)))