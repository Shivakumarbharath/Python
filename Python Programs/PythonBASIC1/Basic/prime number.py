import math

num = int(input('enter a number'))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count += 1
    i = i + 1
if count == 2:
    print('The number is a prime number')
else:
    print('The number is not a prime number')
