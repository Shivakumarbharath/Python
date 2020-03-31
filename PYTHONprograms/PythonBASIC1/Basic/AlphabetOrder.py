str=input("Enter any string to be in Alphabetical order")

lst=[]

for i in str:
    lst.append(ord(i))

lst.sort()
st1=""
for i in lst:
    st1=st1+chr(i)

print(st1)

