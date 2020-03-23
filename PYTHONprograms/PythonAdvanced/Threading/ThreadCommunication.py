from threading import *
import time

class Producer:
    def __init__(self):
        self.productslst=[]
        self.ordersPlaced=False

    #def produce(self):#which will produce the work
