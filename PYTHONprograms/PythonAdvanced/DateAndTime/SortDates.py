from datetime import *
import time
lst=[]
b1=date(2020,2,22)
b2=date(2020,7,23)
b3=date(2020,1,2)


lst.append(b1)
lst.append(b2)
lst.append(b3)

lst.sort()# assending order

lst=lst[::-1] #desecending order

for i in lst:
    print(i)
    time.sleep(1)