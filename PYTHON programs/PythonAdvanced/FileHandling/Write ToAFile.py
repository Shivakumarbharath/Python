f=open("myfile.txt","w")#this opens the file

print("Enter text (Enter $ when done)")
s=" "
while s !="$" :
    s = input()
    f.write(s+'\n')# +"\n " so that every time i use  enter key enter is used in file
f.close()