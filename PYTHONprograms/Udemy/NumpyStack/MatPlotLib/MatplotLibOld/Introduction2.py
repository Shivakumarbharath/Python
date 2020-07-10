import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,20,21)
y1=x**2
y2=x**1.5

print(x,y1)
p=plt.plot(x,y1,"bo-")
#bo is blue circles
#rd means red diamods

#print(p)
plt.show()

