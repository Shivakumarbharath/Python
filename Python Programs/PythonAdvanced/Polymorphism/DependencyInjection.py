# injecting an object into other object

class Flight:
    def __init__(self, engine):  # any type of object can be used
        self.engine = engine

    def Startengine(self):
        self.engine.start()  # here engine is already a object thus object included in parent object


class AirbusEngine:
    def start(self):
        print("AirBus Engine Started Ready for take off")


class BoingEngine:
    def start(self):
        print("Boing Engine ")


# object

a1 = AirbusEngine()
f = Flight(a1)
f.Startengine()

b1 = BoingEngine()

f2 = Flight(b1)

f2.Startengine()
