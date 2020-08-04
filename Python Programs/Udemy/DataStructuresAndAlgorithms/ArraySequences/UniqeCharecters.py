'''

Problem-given astring should contain unique charecters and no repeating charecters

input=avgdi
output-True

input-aabcde
output-False

'''

str = 'asdfg'


def u(str):
    return (len(set(str)) == len(str))


def Uniqe(str):
    for e in str:
        if str.count(e) != 1:
            return False
    return True


def u3(str):
    char = set()
    for e in str:
        if e in char:
            return False
        else:
            char.add(e)
    return True


print(u(str))
print(Uniqe(str))
print(u3(str))
