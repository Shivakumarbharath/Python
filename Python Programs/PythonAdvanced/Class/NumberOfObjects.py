class NumObjects:
    numberOfObj = 0

    def __init__(self):
        NumObjects.numberOfObj = NumObjects.numberOfObj + 1

    def displayCount(numberOfObj):  # to display the cnumber of objects ceated
        print(NumObjects.numberOfObj)


o1 = NumObjects()
o2 = NumObjects()
o3 = NumObjects()

print(o2.displayCount())
