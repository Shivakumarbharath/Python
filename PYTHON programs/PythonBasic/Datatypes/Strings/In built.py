#'' or"" -single line
#'''''' or"""""" - multiple line
name='Bharathz'
name2='BHARGAV'
#find
indexnumber=str.find(name,'a')
print(indexnumber)

#upper
print(name.upper())

#lower
print(str.lower(name2))

#check
check=str.isupper(name)
print(check)

# using str does not change the main value

#captalise only the first letter
name3='fruit'
print(str.capitalize(name3))

# Slicing [start:end+1]
print(name[2:6])

#reverse
print(name[::-1])

# Indexing
print(name[-1]+name[1])

#Replace
print(name.replace('th','t'))

# Split(replace(this)replace)
name4='B,H,a,r,a,t,h'
print(name4.split('a'))

#count
print(name.count('a'))

#max ascii value
print(max(name))

#mix ascii value
print(min(name))

#isalpha
print(name.isalpha())