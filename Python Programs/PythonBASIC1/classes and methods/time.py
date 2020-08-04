class Time:
    def addtime(t1, t2):
        sum = Time()
        sum.hours = t1.hours + t2.hours
        sum.minutes = t1.min + t2.minutes
        sum.sec = t1.sec + t2.sec
        if sum.sec >= 60:
            sum.min += 1
            sum.sec = sum.sec - 60
        if sum.min >= 60:
            sum.hours += 1
            sum.min -= 60
        if sum.hours > 12:
            sum.hours -= 12
        return sum

    def printtime(time):
        print(str(time.hours) + ' ' + str(time.min) + ' ' + str(time.sec))

    def increament(time, sec):
        time.sec += sec
        while time.sec >= 60:  # can give
            if time.sec >= 60:  # while time.sec>=60 and while time.min
                time.sec -= 60
                time.min += 1
            if time.min >= 60:
                time.min -= 60
                time.hours += 1
        return time


currenttime = Time()
currenttime.hours = int(input('Enter the hours'))
currenttime.min = int(input('Enter the minutes'))
currenttime.sec = int(input('Enter the seconds'))
time2 = currenttime.increament(66)
time2.printtime()
