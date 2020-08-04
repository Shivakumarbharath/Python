def createlist():
    lists = []
    limit = int(input('How many elements in the list'))
    for i in range(0, limit):
        print(i, end='')
        a = int(input('th element'))
        lists.append(a)
    return lists


normlist = createlist()
print(normlist)
newlist = normlist[:]
newlist.sort()
print(newlist[0])
