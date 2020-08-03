st=input('Enter a string')
fst=input('enter string to find')
res=st.find(fst)
if res>=0:
    print('Substring Present at ',res)
else:
    print('Subsrtng not present')