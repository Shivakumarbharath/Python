file = input('Enter the file')
i = 0
n = file.index('.') + 1
while n < len(file):
    print(file[n], end='')
    n += 1
