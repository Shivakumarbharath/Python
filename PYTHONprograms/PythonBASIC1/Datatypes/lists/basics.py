#syntax []
camp=['Jason','Tom',800]
print(camp)
#         name   age  qualification
empinfo=['Dustin',32,['Bsc','LLb']]
print(empinfo)
#acccesing
print(empinfo[1])
print(empinfo[2][1])
#range
seq=range(1,10)
print(seq[3])
#range odd[ range( start,stop, steps(difference))
seq1=range(1,10,2)
for i in seq1:
    print(i)

#append ;Changes the main value while for concatination repetation main value no change
camp.append('l')
print(camp)

#extend same as above
camp.extend(['a','b'])
print(camp)

#insert specify indexs position while adding
camp.insert(2,'q')
print(camp)

#pop: removes the specified index  element
camp.pop(2)
print(camp)
days=['Sunday','Monday','Tuesday']
#using for
for day in days:
    print(day)

# to find index
print(camp.index('Tom'))