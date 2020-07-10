import numpy as np
import matplotlib.pyplot as plt


#Create a one dimension array between 0 to 100 with 20 evenly spaced point
x=np.linspace(0,100,1000)

#for y axis
y=np.sin(x)+0.2*x

#Plot it on a graph
#plt.plot(x,y)
##show the graph
#plt.show()


#additional features in the graph
plt.xlabel('Input')#to label the x axis
plt.ylabel('Output')#To label the y axis
p=plt.plot(x,y,"gs-",linewidth=1,markersize=4)#gs is green squares
#bo is blue circles
#rd means red diamods

plt.title('My Plot')#name of the graph

plt.show()