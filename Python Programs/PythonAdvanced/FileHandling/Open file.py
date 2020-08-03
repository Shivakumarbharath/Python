# files are where data is stored

# Syntax variable = open ("filename.extention","mode",buffer)  buffer = 4096 or 8092
'''
modes are:
w =write (all contents will deleted and replaced)
r= read mode
a= append (add new contents)
w+ = write and read
r+= read write and append
a+=appending and reading
x = exclusive creation mode(if other file of same name raises an error)

to deal with binary files append b
ex= wb,rb,w+b etc...
'''

fp = open(r'test.txt', 'w')  # here r means raw which prevents the use of \n \t etc
print(fp)
fp.close()
