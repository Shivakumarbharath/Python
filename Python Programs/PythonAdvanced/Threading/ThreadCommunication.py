'''
To take orders and place orders
Using Boolean Flag

'''

from threading import *
import time


class Producer:
    def __init__(self):
        self.productslst = []  # empty order list
        self.ordersPlaced = False  # using boolean flag

    def produce(self):  # which will produce the work
        for i in range(1, 5):
            self.productslst.append("Products" + str(i))  # to add the items selected in the cart
            print("Item Added")
            time.sleep(1)
            self.ordersPlaced = True  # once all the items are added to cart order is placed i.ie it becomes true


class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def Consume(self):
        while self.prod.ordersPlaced == False:  # untill false not to place order
            time.sleep(2)

        print("Orders Placed", self.prod.productslst)


p = Producer()

c = Consumer(p)

t1 = Thread(target=p.produce())

t2 = Thread(target=c.Consume())
t2.start()
t1.start()
