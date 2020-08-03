'''
A given string contains paranthesis
which is to be balanced
[({})]-ok
{}[)Wrong


'''
d={'[':']','{':'}','(':')'}
k='(){}[(][{)}]'
k=list(k)
e=0
while len(k)>0:
    print(k[e])
    a=k.index(k[e])
    b = k.index(d[k[e]])
    try:
        if (b-a)%2==0:
            print(False)
            exit()
        else:
            k.pop(k.index(d[k[e]]))
            k.pop(k.index(k[e]))
            print(k)
    except ValueError:
        print(False)
        exit()

print(True)
