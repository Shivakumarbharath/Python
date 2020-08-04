from threading import *


class BookMyTicket:
    def __init__(self, availableseats):
        self.availableseats = availableseats
        self.l = Semaphore()  # to make sure of syncronisation

    def buy(self, RequestedSeats):
        self.l.acquire()  # once t his is called any other thread will not access this instance untill realesed
        print(self.availableseats)
        if self.availableseats >= RequestedSeats:
            print("confirming a seat")
            print("Processing")
            print("Sending a mail")
            self.availableseats -= RequestedSeats

        else:
            print("    HouseFull!\nAll Seats Are Booked")
        self.l.release()  # after this other threads can acces this method


t1 = BookMyTicket(10)
t = Thread(target=t1.buy, args=(3,))
t11 = Thread(target=t1.buy, args=(6,))
t22 = Thread(target=t1.buy, args=(3,))

t.start()
t11.start()
t22.start()
