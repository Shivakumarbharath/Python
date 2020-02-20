class time:
    pass
t1=time()
t1.hours=int(input('Enter the hours'))
t1.min=int(input('Enter the minutes'))
t1.sec=int(input('Enter the seconds'))
# t2=time()
# t2.hours=int(input('Enter the hours'))
# t2.minutes=int(input('Enter the minutes'))
# t2.sec=int(input('Enter the seconds'))
def increament(time,sec):
    time.sec+=sec
    while time.sec>=60:# can give
        if time.sec>=60:#while time.sec>=60 and while time.min
            time.sec-=60
            time.min+=1
        if time.min>=60:
            time.min-=60
            time.hours+=1
    return time
time=increament(t1,500)
print(time.hours)
print(time.min)
print(time.sec)