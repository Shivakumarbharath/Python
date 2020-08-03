'''

Problem
Given an integer array and an integer
output all the uniqe pair sum that sum up to the given value
Example-
input-[1,3,2,2],4
output-(1,3)
       (2,2)

Algorithim 1
1.To find the combinations of the given list
2.For every combinations find if sum is equal to k
3.Filter out the combinations that is equal to k


Efficient
Algorithm 2
1.Take a number in list and get
target=k-r
2.find for the target in the same list
3.if found add to as output and pop out the target from the list

'''
i=[4,5,7,8,9,1,2,3,3,5]
k=10


def ArrayPair(lst,k):
    import itertools
    comb=list(itertools.combinations(lst,2))
    fil=filter(lambda x:x[0]+x[1]==k,comb)
    print(list(fil))

#Best Algorithm
def pair_sum(lst,k):
    if len(lst)==2:
        return
    seen=set()
    output=set()
    for num in lst:
        target= k-num
        if target not in seen:
            seen.add(num)#add it to avoid being tested again
        else:
            output.add((min(num,target),max(num,target)))
    print('\n'.join(map(str,list(output))))


def pai_sum_2(lst, k):
    if len(lst) == 2:
        return
    new_lst=[]
    for num in lst:
        target = k - num
        if target==num:
            num = lst.pop(lst.index(num))

        #print(target)
        if target in lst:
            target2=lst.pop(lst.index(target))
            new_lst.append((min(num, target2), max(num, target2)))

        else:
            continue

    print('\n'.join(map(str, new_lst)))



#ArrayPair(i,k)
pair_sum(i,k)
print()
print()
pai_sum_2(i, k)