class Time:
    def after(self,time2):
        if self.hours>time2.hours:
            return 1
        else:
            return 0
t1=Time()
t1.hours=int(input('Enter the hours'))
t1.min=int(input('Enter the minutes'))
t1.sec=int(input('Enter the seconds'))
t2=Time()
t2.hours=int(input('Enter the hours'))
t2.min=int(input('Enter the minutes'))
t2.sec=int(input('Enter the seconds'))
status=t1.after(t2)
print(status)
#optional arguments give an extra argument with start = default valuve
#if an argument is given then start gets overriden
