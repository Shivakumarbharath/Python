lists=[]
i=0
sum=0
limit=int(input('How many elements in the list'))
for i in range(0,limit):
    print(i,end='')
    a=int(input('th element'))
    lists.append(a)
    sum=sum+lists[i]
print(lists)
print(sum)