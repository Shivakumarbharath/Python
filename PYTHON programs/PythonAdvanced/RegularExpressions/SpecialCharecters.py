'''

\ escape charecters - if u want to use any special charecters in regular expressions  then it is used to escape it
. dot operater- which matches any charecter exept a new line
^ - used to match the regular expression at the beggining of the string
$ "       "                      "               end  """

[...] - matches a range of  values within it (between it)
[^...]- matches every charecter excpt the values between the values provided
 ( )  match the regular expression
  |- this is used to specify  multiple regular expression (R|S)

'''


import re

st="1  One by One 2 I will achieve 3 success  Ohg Okk Off On Of Ok"

result=re.search(r'$ O\w',st)# now it searchs for a patterno\w\w and replace with two

print(result)

result=re.search(r'O\w\w',st)# now it searchs for a patterno\w\w and replace with two

print(result)