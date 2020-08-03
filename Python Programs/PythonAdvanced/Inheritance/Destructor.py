import time
import gc
class Test:
    def __init__(self):
        print('object init')
    def __del__(self):
        print('full fil .....')
print(gc.isenabled())
t1=Test()
t2=t1
t3=t2
del t1
time.sleep(10)
print('objects not yet destroyed,after deleting t1')
del t2
time.sleep(10)
print('objects not yet destroyed,after deleting t2')
del t3
time.sleep(10)
print('objects is destroyed,after deleting t3')
#Destruction is possible only when all the object reference is deleted
