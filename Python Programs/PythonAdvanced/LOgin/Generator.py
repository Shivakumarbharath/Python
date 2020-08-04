def f1(a=0):
    while True:
        a = a + 1
        yield a


go = f1(656)
print(next(go))
print(next(go))
