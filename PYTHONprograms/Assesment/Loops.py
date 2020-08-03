'''

Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

'''
#soln

# for k in range(1500,2701):
#     if (k%5==0) and (k%7==0):
#         print(k)
#

'''
 Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
#soln

# h=3
# for i in range((h*2)):
#     if i <=h:
#         print('* '*i)
#     else:
#         print('* '*(h*2-i))


'''
Write a Python program that prints each item and its corresponding type from the following list.
Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

'''
# datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
# for e in datalist:
#     print(e,type(e))



'''

Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5

'''
# for i in range(7):
#     if i !=0:
#         if i%3==0:
#             continue
#     print(i)

'''

Python Exercise: Fibonacci series between 0 to 50


'''

# x,y=0,1
#
# while y<50:
#     print(y)
#     x,y = y,x+y


'''
Write a Python program which takes two digits m (row) and 
n (column) as input and generates a two-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.

Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

'''
Rows = 3
Columns = 4

final=[[row*column for column in range(Columns)] for row in range(Rows)]

# for row in range(Rows):
#     final.append([])
#     for column in range(Columns):
#         final[row].append(row*column)

print(final)

for i in range(1, 5):
    for k in range(1,i):
        print(k, end='')
    print()
k=[[j for j in range(1,i)] for i in range(2,5)]

print(k)