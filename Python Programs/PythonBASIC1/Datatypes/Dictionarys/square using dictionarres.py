def square(n):
    square = {}
    for i in range(1, n + 1):
        square[i] = i ** 2
    return square


result = square(10)
print(result)
