'''I have 3 lists and one string like this:

a = ['a', 'b', 'c']
b = [1, 2, 3, 4, 5]
c = [10, 11, 14, 15, 16]
string = 'buy'

I need a list of dictionary like this:

[{'a':1 , 'b':10 , 'c':'buy'},{'a':2 , 'b':11 , 'c':'buy'},{'a':3 , 'b':14 , 'c':'buy'},...]
'''

a = ['a', 'b', 'c']
b = [1, 2, 3, 4, 5]
c = [10, 11, 14, 15, 16]

lst = [{'a': x, 'b': y, 'c': 'buy'} for x, y in zip(b, c)]

'''
lst=[]
for x,y in zip(b,c):
    lst.append({'a':x,'b':y,'c':'buy'})
'''
print(lst)
