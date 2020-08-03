from threading import *
from time import sleep

def DisplayNumbers():#step 1 define a function
    i=0
    print(current_thread().getName(),end="\n")# it will be in the thread
    sleep(1)
    while(i<=10):
        print(i,end="\n")

        i+=1


print(current_thread().getName())# it will be in main thread
t=Thread(target=DisplayNumbers) #Step 2 - create an object
t.start()


t1=Thread(target=DisplayNumbers) #Step 2 - create an object
t1.start()


t2=Thread(target=DisplayNumbers) #Step 2 - create an object
t2.start()
