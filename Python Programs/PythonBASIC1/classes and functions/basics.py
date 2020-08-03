class time:
    pass
t1=time()
t1.hours=int(input('Enter the hours'))
t1.minutes=int(input('Enter the minutes'))
t1.sec=int(input('Enter the seconds'))
t2=time()
t2.hours=int(input('Enter the hours'))
t2.minutes=int(input('Enter the minutes'))
t2.sec=int(input('Enter the seconds'))
# if t1.hours>t2.hours and t1.minutes>t2.minutes and t1.sec>t2.sec:
#     print(True)
# print(t1.hours,':',t1.minutes,':',t1.sec)
# print(t2.hours,':',t2.minutes,':',t2.sec)
def addtime(t1,t2):
    sum=time()
    sum.hours=t1.hours+t2.hours
    sum.minutes=t1.minutes+t2.minutes
    sum.sec=t1.sec+t2.sec
    if sum.sec>=60:
        sum.minutes+=1
        sum.sec=sum.sec-60
    if sum.minutes>=60:
        sum.hours+=1
        sum.minutes-=60
    if sum.hours>12:
        sum.hours-=12
    return sum
ntime=addtime(t1,t2)
print(ntime.hours,':',ntime.minutes,':',ntime.sec)
