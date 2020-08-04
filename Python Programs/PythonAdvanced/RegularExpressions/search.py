import re

# r means regular expresions

st = "1 One by one 2 I will achieve 3 success  ohg okk off"

result = re.search(r'o\w\w', st)  # this statment returns the string startng with and two letter after it

print(result)  # .group to view what is in result

print(result.group())  # .group to view what is in result

print(result.span())  # .group to view what is in result in which place it is contained

result = re.findall(r'o\w\w', st)  # to find all the the words with the patern . It returns a list

print(result)

result = re.match(r'o\w\w', st)  # same as search but finds only at the begining

print(result)

result = re.match(r'O\w\w', st)  # finds only at the begining

print(result)  # if anser is none error arises for .group

result = re.split(r'\d+', st)  # to split from the digit (d) for more than 1 such digits (+)

print(result)

result = re.sub(r'o\w\w', 'two', st)  # now it searchs for a patterno\w\w and replace with two

print(result)
