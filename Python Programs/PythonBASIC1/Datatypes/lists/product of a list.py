lists = []
i = 0
prod = 1
limit = int(input('How many elements in the list'))
for i in range(0, limit):
    print(i, end='')
    a = int(input('th element'))
    lists.append(a)
    prod = prod * lists[i]
print(lists)
print(prod)
