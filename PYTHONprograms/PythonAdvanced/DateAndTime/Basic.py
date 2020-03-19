import time,datetime

epochtime=time.time()
print(epochtime)

t=time.ctime()
print(t)

print(time.ctime(epochtime))
tt=datetime.datetime.today()
print("Currrent DAte : {}\{}\{}".format(tt.day,tt.month,tt.year))