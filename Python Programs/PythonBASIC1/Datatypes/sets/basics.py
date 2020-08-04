# syntax {}
myset = {1, 2, 3, 5, 8, 9, 2, 6}
print(myset)
print(type(myset))

# union
myset2 = {3, 9, 7, 10, 50, 13, 22}
print('union=', myset | myset2)

# intersection
print('intersection=', myset & myset2)

# difference
print('difference1=', myset2 - myset)
print('difference2=', myset - myset2)
