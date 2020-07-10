'''


Matplotlib is a Python plotting library that
produces publication-quality figures.
It can be used both in Python scripts and when
using Python's interactive mode.
Matplotlib is a very large library, and getting to know it well takes time.
But often we don't need the full matplotlib library in our programs,
and this is where Pyplot comes in handy.
Pyplot is a collection of functions that make matplotlib work like Matlab,
which you may be familiar with.
Pyplot is especially useful for interactive work,
for example, when you'd like to explore a dataset
or visually examine your simulation results.
We'll be using Pyplot in all our data visualizations.
Pyplot provides what is sometimes called a state machine
interface to matplotlib library.
You can loosely think of it as a process where you create figures one at a time,
and all commands affect the current figure and the current plot.
We will mostly use NumPy arrays for storing the data that we'd
like to plot, but we'll occasionally use other types
of data objects such as built-in lists.
As you may have realized, saying matplotlib.pyplot
is kind of a mouthful, and it's a lot to type too.
That's why virtually everyone who uses the library
imports it as plt, which is a lot shorter.
So to import the library, we will type the following-- import
matplotlib.pyplot as plt.
Now we are ready to start our plotting.
A basis but very useful command is the plt plot function, which
can be used to plot lines and markers.
The simplest version of plot has just one argument,
and it specifies the y-axis values that are to be plotted.
In this case, when you provide just one argument, the plot function,
each y-axis value will be plotted against its corresponding index value
on the x-axis.
Because Python indexing starts at 0, the first element of your array or list
appears at location x equal to 0.
The second element appears at location x equal to 1, and so on.
Let's now practice using the plot function in the IPython Shell.
Let's start by making a simple plot.
So we'll say plt.plot.
I'm going to create a list consisting of the numbers 0, 1, 4, 9, and 16.
You can see here that Python returns a matplotlib object.
If for some reason you'd like to suppress the printing of that object,
in the IPython Shell you can add a semi-colon at the end of the line
and that will do the job.
If we rerun this with the semi-colon at the end,
you'll see that the plot still appears, but we don't
get that matplotlib object printed out.
Because we are working in IPython, the plots
will appear inside the Python Shell.
Well, let's see what happens if, instead of using IPython Shell,
we used the standard Python Shell.
Let's first launch the Python Shell.
I'm going to go to View Panes and Console.
I'll resize my window a little bit.
Because we have a new session here, I need to do my import first.
So I've just imported my plt.
The next step is to create the plot 0, 1, 4, 9, and 16.
You'll notice that it seems like nothing has happened.
In fact, the plot has been created, but because we are not
working in a Python Shell, not IPython Shell,
we need to issue the command Show for plt to show the plot.
So let's try that-- plt.show.
We can also give the plot function two arguments, in which case
the first argument specifies the x-coordinates of the points,
and the second argument the y-coordinates of the points.
I'm going to create a vector x using np.linspace.
I want that vector to start at 0 and at 10,
and I would like to have 20 points in my vector-- in my one-dimensional array.
I'm going to define my y-vector from the x.
I'm going to be taking every element of x and raising them to power 2.
Now I have two vectors defined-- x and y.
I can now call the plot function where my first argument
is x and my second argument is y.
In this case, what we have is the familiar shape of a parabola.
We can also provide a third argument to the plot
function, which is a format string that specifies color, marker, and line type.
Letters and symbols of the format string are the same as in Matlab,
but even if you're not familiar with those,
you'll easily learn them with a little practice.
This is also a good place to introduce what are called keyword arguments.
The idea is completely generic and applies to all Python functions,
but with the plt library, it's almost impossible not to use them.
In short, a keyword argument is an argument
which is supplied to the function by explicitly naming each parameter
and specifying its value.
Two keyword arguments that I use all the time are linewidth and markersize.
Let's put these different ideas together in an example.
I'm first going to create my vector x.
It's a linear vector starting from 0, going to 10, and consists of 20 points.
I'm going to define y1, which is going to be my x raised to the power of 2.
Then I'm going to define a second vector.
Let's call that y2, and this is x raised to the power of 1.5.
At this point, I have three vectors-- x, y1, and y2.
I can now call the plot function.
My first argument is x, my second argument is y1,
and then my third argument specifies the appearance of the plot.
In this case, I'm requesting plt to use blue, to use circles,
and to use a solid line.
We can try plotting this out, and we see the outcome.
We can now add our keyword arguments to this function call.
I can specify linewidth.
I'm going to set it to 2 in this case.
I'm going to also specify markersize, which I'm going to set to 4.
And in this case, you'll see that the linewidth has changed,
and the size of the markers has also changed.
If I would prefer larger markers, I could set markersize 12
and, again, the effect is apparent.
I can do the same thing for y2.
I'm going to use this line and build from it.
I'm going to be plotting x, and I'm going to be plotting y2
but in this case, I would like to use green squares,
so I change b to g, meaning from blue to green. And I change circles to squares,
so I change the o to an s. And I will still stick with my solid lines.
In this case, we run the line and we see the green plot.


'''
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,20,21)
y=x**2

print(x,y)
p=plt.plot(x,y)

#print(p)
plt.show()





































