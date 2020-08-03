from threading import *


def DisplayNumbers():  # step 1 define a function
    i = 0
    print(current_thread().getName())  # it will be in the thread
    while (i <= 10):
        print(i)
        i += 1


print(current_thread().getName())  # it will be in main thread
t = Thread(target=DisplayNumbers)  # Step 2 - create an object
t.start()
