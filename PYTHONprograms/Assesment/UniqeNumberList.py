'''

Create a function that takes a list of numbers and return the number that's unique.

Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7

unique([0, 0, 0.77, 0, 0]) ➞ 0.77

unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0






lst=input("Enter").split(' ')
print(lst)
for i,e in enumerate(lst):
    if i+2 >len(lst)-1:
        print(lst[-1])
        break

    if e != lst[i+1]:
        if i+2 == (len(lst) - 1):
            if lst[0] == lst[len(lst)-1]:
                print(lst[-2])
                break
        if lst[i+1] !=lst[i+2]:
            print(lst[i+1])
            break
        else:
            print(e)
            break



'''
#Alternative
lst=input("Enter").split(' ')
def unique(lst):
    print(lst.count('5'))
    return min(lst, key=lst.count)

print(unique(lst))

