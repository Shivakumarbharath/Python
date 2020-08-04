# Abstraction = To make any one or more method in parent class manadatory to be used in child class
# now bmw wants all the series or cars inheriting its class must and should have the method called drive
# implementing this is called abstraction and class with abstract methed is absrtract class
# An abstract class cannot be instantiated ie., objects of that class cannot be created only child classes can be created
# two steps to implement it
# 1. from lib abc import abstraction method
# 2.inherit ABC into abstract class
# before the abstrat method use @abstractmethod
from abc import abstractmethod, ABC


class BMW(ABC):
    def __init__(self, year, model, make):
        self.year = year
        self.model = model
        self.make = make

    def Start(self):  # this ca be used in any child class objects
        print("Car Started appliying gear")

    def Stop(self):
        print("Applying Brakes \n Car stopped")

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):  # inheriting the properties of BMW
    def __init__(self, cruisecontrol, year, model, make):
        BMW.__init__(self, year, model,
                     make)  # using the properties of BMW and also same as super().__init__(year,model,make)
        self.cruisecontrol = cruisecontrol

    def Start(self):  # if same name is used in child class for different functionality the method is overridden
        print("Please Press the button")
        super().Start()  # adding the functionality of BMW start

    def drive(self):
        print("Three Series is being driven")


class FIveSeries(BMW):  # inheriting the properties of BMW
    def __init__(self, ParkingAssistnce, year, model, make):
        BMW.__init__(self, year, model, make)  # using the properties of BMW
        self.ParkingAssistnce = ParkingAssistnce

    def drive(self):
        print("Five Series is being driven")


B3 = ThreeSeries(True, "2020", "620i", "WolksWagan")
B5 = FIveSeries(True, "2022", "68g duo", "WolksWagan")

print(B5.ParkingAssistnce)
print(B5.make)
print(B5.model)
print(B5.year)

B3.Start()

B3.Stop()

print("  ")

print(B3.cruisecontrol)
print(B3.make)
print(B3.model)
print(B3.year)

B5.Start()

B5.Stop()
