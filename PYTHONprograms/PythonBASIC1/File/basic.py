# #syntax
# #f=open("File Name","r or w")
# f=open("File.txt","r")
# #f.write()
# text = f.read()
# print(text)
# f.close()

f=open("book.txt",'w')
f.write("line 1\n line 2\n line 3")
f.close()
f=open("book.txt",'r')
text=f.readline(2)# to read a particular line ;mutiple lnes use readlines
print(text)