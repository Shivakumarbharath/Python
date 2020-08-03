from threading import *


class MyThread(Thread):# creating a thread super class
    def run(self):# overriding the run method
        i = 0
        print(current_thread().getName())  # it will be in the thread
        while (i <= 10):
            print(i)
            i += 1

t=MyThread() #create an instance
t.start()# to get into the thread