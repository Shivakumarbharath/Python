from threading import Thread


class BookMyTicket:
    def buy(self):
        print("confirming a seat")
        print("Processing")
        print("Sending a mail")


t1 = BookMyTicket()
t = Thread(target=t1.buy)  # Step 2 - create an object
t11 = Thread(target=t1.buy)  # Step 2 - create an object
t22 = Thread(target=t1.buy)  # Step 2 - create an object

t.start()
t11.start()
t22.start()
