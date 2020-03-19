import sys
import os
print(sys.argv)
print(dir(os))

import threading

th=[]

def f(i):
    print(i,'= thread' )

for i in range(5):
    t=threading.Thread(name=i,target= f, args =(i,))
    th.append(i)
    t.start()
    t.join()
print(th)