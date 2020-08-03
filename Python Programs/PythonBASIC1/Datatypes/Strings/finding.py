def find(str,char):
    i=0
    while i<len(str):
        if char==str[i]:
            return i
        else:
            i= i+1
a=find('Bharath','a')
print(a)