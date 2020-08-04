def Pyramid(n, stri):
    for i in range(1, n + 1):
        print(' ' * (n - i) + (stri + ' ') * i)


Pyramid(10, '*')
