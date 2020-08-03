#the head of the list
numbers=[1,2,3,5,4,6]
def head(list):
    return list[0]

a=head(numbers)
print(a)
def delete(list):
    del head(list)

#tail
def tail(list):
    return list[5]


a = tail(numbers)
print(a)
