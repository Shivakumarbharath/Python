from datetime import *
import time
start_time=time.perf_counter()# it gives the performance time that is exact time from start of execution
print(start_time)

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


end_time= time.perf_counter()#same as above

print("Time for Executing the code is ",end_time)# time taken from start time to end time