lst=[1,2,3,4,5,6,7]
fp=open(r'test2.txt','w')
fp.write('Test header\n')
fp.write('Test detailes')
fp.close()

#to open more files

with open(r'text.txt','w') as fp:
    fp.write('Test header\n')
    fp.write('Test detailes\n')
    fp.write('[1,2,3,4,5,6,5]')

with open(r'text.txt','r') as fp:
    t1=fp.readline()#eval to find the datatype
    print(type(t1))