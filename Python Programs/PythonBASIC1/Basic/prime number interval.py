range1 = int(input('Enter from which number :'))
range2 = int(input('To which number :'))
c = range1


def prime(num):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i = i + 1
    if count == 2:
        print(num)


while c <= range2:
    prime(c)
    c += 1
