import numpy as np
import matplotlib.pyplot as plt

x=np.random.randn(100,2)
#as they are 2d there should be in 2d
plt.scatter(x[:,0],x[:,1])#(x axis ,y axis)
#x[:,0] first column of x
#x[:,1] second column of x
#plt.show()

y=np.random.randn(200,2)

y[:100]+=3#add 3 to all half of the elements of x

y2=np.zeros(200)

y2[:100]=1

plt.scatter(y[:,0],y[:,1],c=y2)
plt.show()

print(y)
print(y2)