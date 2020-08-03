def createlist():
    lists = []
    limit = int(input('How many elements in the list'))
    for i in range(0, limit):
        print(i, end='')
        a = int(input('th element'))
        lists.append(a)
    return lists


even = createlist()
for i in range(0, len(even)):
    if even[i] % 2 != 0:
        print(even[i])
