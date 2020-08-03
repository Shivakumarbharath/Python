''''
here using wait() and notify() and notifyAll()
use condion library
'''

from threading import *
import time

class Producer:
    def __init__(self,):
        self.productslst=[]# empty order list
        self.c=Condition() #to use wait and notify


    def produce(self):#which will produce the work
        self.c.acquire() #To lock the instance
        for i in range(1,5):
            self.productslst.append("Products"+str(i) )# to add the items selected in the cart
            print("Item Added")
            time.sleep(1)
        self.c.notify()#to notify the other thread to take over
        self.c.release()




class Consumer:
    def __init__(self,prod):
        self.prod=prod


    def  Consume(self):

        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)#to wait till it notify after which the below lines are executed
        self.prod.c.release()
        print("Orders Placed",self.prod.productslst)



p=Producer()

c=Consumer(p)


t1=Thread(target=p.produce())

t2=Thread(target=c.Consume())
t2.start()
t1.start()

