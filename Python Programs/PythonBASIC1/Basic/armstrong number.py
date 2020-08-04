num1 = int(input('Enter a number'))
num = num1
n = 10
i = 0
while num // n != 0:
    i += 1
    n = n * 10
d = i + 1
n = 10
sum = 0
while num // n != 0:
    sum = sum + ((num % n) ** d)
    num = num // 10
sum = sum + ((num % n) ** d)

if sum == num1:
    print('The number is armstrong')
else:
    print('Number is not armstrong')
