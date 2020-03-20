from threading import *


class MyThread:# without inheriting the Thread superclass
    def DisplayNumbers(self):# overriding the run method
        i = 0
        print(current_thread().getName())  # it will be in the thread
        while (i <= 10):
            print(i)
            i += 1

obj=MyThread() #create an object
t=Thread(target=obj.DisplayNumbers)#creat an instance
t.start()# to get into the thread