import re

st = "02-12-2020  , 02-11-2000"
result = re.findall(r'\d{0,2}-\d{2}-\d{4}', st)

print(result)
