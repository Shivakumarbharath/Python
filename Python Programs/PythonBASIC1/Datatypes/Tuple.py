# Syntax ()
mytuple = ('Bharath', 18, 2000, 'Python')

# concatination
print(mytuple + ('d', 'f'))

print(mytuple)


# Repetation same as strnig
# slicing same as string
# indexing same as string
# its immutable (only difference from lists)
# mytuple[2]='2010'  cannot be changed

# swap
def swap(a, b):
    return b, a


result = swap(10, 5)
print(result)
# can include list in tuble and vice versa
