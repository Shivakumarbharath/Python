class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    class Engine:  # class inside a class
        def __init__(self, num):
            self.num = num

        def Start(self):
            print("EngineStarted")


c1 = Car("BMW", 2020)  # the outer class is created
c1e = c1.Engine("AmBmW5566982")  # the inner class is created

c1e.Start()
