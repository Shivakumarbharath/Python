class Product: #class creation
    def __init__(self):# initialisation this executes only once when class is created
        self.name="Lamborgini"#name
        self.price="200000000"#price
        self.description="Latest Xs5"#description
    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

c1=Product()#object creation

c1.display()


