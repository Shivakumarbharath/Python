'''

Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

'''
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

k = filter(lambda x: x if (x % 19 == 0) or (x % 13 == 0) else False, nums)

print(list(k))
