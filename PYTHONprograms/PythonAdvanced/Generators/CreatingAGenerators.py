# Generators are function that returns a sequence of values back
# a generator uses a yeild statment
# using the yeild we can store each value in sequence
# at the end of the sequence generation we will return the entire sequence
def customran(x, y):
    while x <= y:
        yield x
        x += 1


print(list(customran(5, 35)))
