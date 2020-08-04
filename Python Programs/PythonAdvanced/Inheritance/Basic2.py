# Inheritance is the process of defining a new object with a help of existing object

class BMW:
    def __init__(self, year, model, make):
        self.year = year
        self.model = model
        self.make = make

    def Start(self):  # this ca be used in any child class objects
        print("Car Started appliying gear")

    def Stop(self):
        print("Applying Brakes \n Car stopped")


class ThreeSeries(BMW):  # inheriting the properties of BMW
    def __init__(self, cruisecontrol, year, model, make):
        BMW.__init__(self, year, model,
                     make)  # using the properties of BMW and also same as super().__init__(year,model,make)
        self.cruisecontrol = cruisecontrol

    def Start(self):  # if same name is used in child class for different functionality the method is overridden
        print("Please Press the button")
        super().Start()  # adding the functionality of BMW start


class FIveSeries(BMW):  # inheriting the properties of BMW
    def __init__(self, ParkingAssistnce, year, model, make):
        BMW.__init__(self, year, model, make)  # using the properties of BMW
        self.ParkingAssistnce = ParkingAssistnce


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
