import matplotlib.pyplot as plt

import numpy as np
x1=np.logspace(-1,20,21)
y1=x1**2
y2=x1**1.5

x=np.random.gamma(2,3,100000)
plt.hist(x1,bins=np.linspace(-5,5,20))
plt.loglog(x1,y1,"gs-",linewidth=2,markersize=4,label="First")
plt.hist(x,bins=30,cumulative=True,histtype="step")
plt.show()