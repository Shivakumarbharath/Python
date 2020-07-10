import numpy as np
import matplotlib.pyplot as plt



n=10000
hal=n//2
quat=hal//2
quat_3=hal+quat
#x=np.zeros((n,2))


x=np.random.randn(n,2)

k=4
x[:,0][:hal]=(x[:,0][:hal]-k)/(k+2)
x[:,0][hal:]=(x[:,0][hal:]+k)/(k+2)
x[:,1][0:quat]=(x[:,1][0:quat]-k)/(k+2)
x[:,1][quat:hal]=(x[:,1][quat:hal]+k)/(k+2)
x[:,1][hal:quat_3]=(x[:,1][hal:quat_3]-k)/(k+2)
x[:,1][quat_3:]=(x[:,1][quat_3:]+k)/(k+2)


y=np.ones(n)
y[:quat]=0
y[quat_3:]=0
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()
