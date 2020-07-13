'''
Write a NumPy program to test whether none of the elements of a given array is zero.

'''
import numpy as np


print(np.all([0,2,3,4]))#Test whether all array elements along a given axis evaluate to True.
'''
Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).

Sample Solution :

Python Code :

'''

a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))