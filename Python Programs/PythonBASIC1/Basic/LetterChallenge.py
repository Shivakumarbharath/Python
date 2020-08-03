'''

in this challenge the input will be a string and output will be letters enxrt to the string
for example input a outbut is b
and if output is vowels then it should be in capital letters
'''

st = input("enter a string")

st1 = ""

for i in st:
    k = ord(i)
    if k == 122:
        k = 97
    elif k >= 97 and k < 122:
        k = ord(i) + 1
    else:
        k = ord(i)

    st1 = st1 + chr(k)

for i in st1:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        j = i.upper()
        st1 = st1.replace(i, j)

print(st1)
