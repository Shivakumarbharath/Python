list = [x for x in
        input('enter the numbers seperated by comms').split(',')]  # the value will be stored as a string by default
print(list)
list = [int(x) for x in input('enter the numbers seperated by comms').split(
    ',')]  # the value will be stored as a integer and can be changed if required
print(list)

# x is a intermediate variable and for loop
#     the above equvivalent to

b = input('enter the numbers seperated by comms').split(',')
list = []
for x in b:
    list.append(int(x))
    print(x)

print(list)
