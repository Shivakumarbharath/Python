'''

t of transcript. Skip to the end.
In some plots, it's helpful to have one or both axes be logarithmic.
This means that for any given point to be plotted, its x or y-coordinate,
or both, are transformed using the log function.
So what ends up being plotted on the x-axes
is not the original x-coordinate, but instead the value of log x.
The logarithm is taken by default in base 10.
So if, for example, log of 100 is equal to 2,
but the base can be specified to be something else as needed.
The plt functions that I used to make logarithmic plots are the following--
semilogx() plots the x-axes on a log scale and the y in the original scale;
semilogy() plots the y-axes on the log scale and the x in the original scale;
loglog() plots both x and y on logarithmic scales.
To plot both x and y on the original scales,
you can use to plt function we have just discussed, plt.plot.
To understand why logarithmic plots are sometimes useful, let's
take a quick look at the underlying math.
Consider a function of the form y is equal to x the power of alpha.
y is equal to x to the power of alpha.
If alpha is equal to 1, that corresponds to a line that goes through the origin.
Alpha equal to half gives you the square root, and alpha equal to 2
gives us a parabola.
Let's see what we can do with this equation.
We're first going to take logs of both sides, which gives us
log of y is equal to log of x to alpha.
You may remember that in the logarithm, we can pull the exponent here
to the front of the expression.
Let's do just that, in which case we end up with alpha being at the front.
So our alpha ends up being over here.
In this case, what we have is log y is equal to alpha times log of x.
We can now think about plotting this on a different set of axes,
where instead of using our original y, we have log transformed the axes.
I'm going to call this y prime.
I'm going to do the same for my x.
My alpha stays put.
So my log x becomes x prime.
So you'll see that on these new axes, we have a much simpler equation.
Y prime is equal to alpha times x prime.
So let's look at this as a plot.
Let me erase my starting point here.
We have our new axes here.
We have our x prime, and we have our y prime here.
The shape of this function is going to be simply a line that looks like this.
In this case, alpha is going to be given by the slope of this line.
So the lesson here is that functions of the form y is equal to x to power alpha
show up as straight lines on a loglog() plot.
The exponent alpha is given by the slope of the line.
Let's look at an example of a loglog() plot.
I'm going to work here with my previous plot.
Instead of using the plt.plot function, I'm going to replace the plot with
loglog() and I will do that for both y1 and y2.
We will then re-run this.
And in this case, we are plotting the functions on a loglog() scale.
If you wanted even spacing on the x-axes,
we can generate numbers that are evenly spaced, not
on a linear scale which is what we get from np.linspace,
but on the logarithmic scale.
To accomplish this, we can use the np.logspace function.
I'm going to go back to my plot, but instead of linspace,
I replace lin with log.
Now, I need to be careful with the start and end points.
I'm going to start from minus 1.
Remember that means that my first point is going to be 0.1.
I'm going to end at 1, which is 10 to 1, meaning the endpoint is equal to 10.
In this case, I'm going to modify the number of points.
Let me go with 40.
We can now re-run the plot.
And here, we see the result of using logspace.
In this case, all of the points along the x-axis are evenly spaced.


'''


import numpy as np
import matplotlib.pyplot as plt

x=np.logspace(-1,20,21)
y1=x**2
y2=x**1.5

print(x,y1)
plt.loglog(x,y1,"gs-",linewidth=2,markersize=4,label="First")#gs is green squares
plt.loglog(x,y2,"rd-",linewidth=2,markersize=4,label="Second")
plt.legend(loc="upper left")#to  diplay the labels of the plot
plt.xlabel("$X$")#dollor gives an italian look
plt.ylabel("$Y$")
#plt.axis([.5,30,-50,400])#Limit the window axes
# plt.axis([xmin,xmax,ymin,ymax])
#plt.savefig("myplot.png")# to save the figure
#print(p)
plt.show()

