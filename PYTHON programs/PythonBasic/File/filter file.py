f1=open("book.txt",'r')
f2=open("dup.txt",'w')
while True:
    text=f1.readline()
    if text=="":
        break#terminate the main while loop (executes below statments)
    if text[0]=='#':
        continue # to continue from main while loop (does not executes the below statments)
    f2.write(text)
f1.close()
f2.close()