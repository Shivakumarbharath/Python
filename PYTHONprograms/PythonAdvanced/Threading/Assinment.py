'''

to  creat a 2 threads even and odd
'''

from threading import *



def EvenNumbersThread():



    for i in range(0,101,2):



         print(i)



def OddNumbersThread():



    for i in range(1,101,2):



        print(i)



t1 = Thread(target =EvenNumbersThread)



t1.start()



t2 = Thread(target = OddNumbersThread)



t2.start()



for i in range(0,101):

    print(i)