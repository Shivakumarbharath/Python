def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
ran=int(input('Enter the range'))
for i in range(0,ran):
    print(fib(i))