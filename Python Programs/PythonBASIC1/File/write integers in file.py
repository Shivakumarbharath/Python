f = open("File.txt", 'w')
x = 654
f.write(str(x))
f = open("File.txt", 'r')
text = f.read()
print(text)
# to include integers in strings
# '%d%d%d'%(3,2,3)
# to get a output-
