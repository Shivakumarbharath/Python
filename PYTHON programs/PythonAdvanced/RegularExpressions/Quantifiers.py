'''
+ * ?  {m}are quantifierss
+ means one or more
ex \d+ means one or more digits
* means 0 or more
? means 0 or 1 such thing
{m}  exactly m ocurances
{m,n} min m and max n
'''
import re
# r means regular expresions

st="1 One by One 2 I will achieve 3 success  Ohg Okk Off On Of Ok"


result=re.findall(r'O\w+',st)# now it searchs for a patterno\w\w and replace with two

print(result)


result=re.findall(r'O\w?',st)# now it searchs for a patterno\w\w and replace with two

print(result)


result=re.findall(r'O\w{1}',st)# now it searchs for a patterno\w\w and replace with two

print(result)

result=re.findall(r'O\w+',st)# now it searchs for a patterno\w\w and replace with two

print(result)