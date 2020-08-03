def FirstFactorial(num):
    if num != 1:
        return num * FirstFactorial(num - 1)
    else:
        return num


print(FirstFactorial(int(input())))
