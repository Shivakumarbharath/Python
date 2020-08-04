import numpy as np

'''
having two equations and two unknown

example
1.5x+4y=5050
x+y=2200

formula for the problem 

AX=B
X=inverse(A)B

here X=[[x],[y]]
A=[[1,1],[1.5,4]]
B=[[2200],[5050]]

This is not done in code
Because 
1.The inverse is slower and less accurate
2.There are better algoriths to solve them

It is done using the solve method in the linalg class


result=np.linalg.solve(A,B)

'''

A = np.array([[1, 1], [1.5, 4]])
B = np.array([2200, 5050])

result = np.linalg.solve(A, B)

print(result)
