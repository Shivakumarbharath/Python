'''
Write a function that moves all elements of one type to the end of the list.

Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]


'''

ls = [1, 3, 2, 4, 4, 1]
el = 1
cnt = ls.count(el)
for i in range(0, cnt):
    ls.remove(el)
    ls.append(el)

print(ls)

'''
Alternative 

def move_to_end(lst, el):
	return [x for x in lst if x!=el]+[el]*lst.count(el)
	
	
	'''
