lst = ["78, 3, 5, 7, 198", "1, 2, 4, 13, 15"]
lst1 = lst[0]
lst2 = lst[1]
lst1 = lst1.split(',')
for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
lst2 = lst2.split(',')
for i in range(len(lst2)):
    lst2[i] = int(lst2[i])
res = []
for i in lst1:
    for j in lst2:
        if i == j:
            res.append(i)
if len(res) == 0:
    print("False")
for i in range(len(res)):

    if i == (len(res) - 1):
        print(res[i])
    else:
        print(res[i], end=",")
