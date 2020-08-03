'''

Start of transcript. Skip to the end.
There are a few important elements that can be easily added to plots.
For example, we can add a legend with the legend function.
We can adjust axes with axis, where axis is spelled A-X-I-S.
We can set axis labels using xlabel and ylabel.
And we can save a figure using savefig.
In that case, the file format extension specifies the format of the file,
such as pdf or png.
Let's now add these elements to our previous plot.
I'm going to construct this plot in the editor.
So I'm going to take my first line and place that in the editor.
Then I'm going to take my second line and just copy paste that in the editor.
If I want to construct the full plot, I'm
going to find my definition of x, so we have a full example,
x was defined here.
Then we had definitions of y1, which was given here.
And we have also our definition of y2, which is here.
This is the plot that we've been looking at so far.
I'm going to start by adding axes labels to this plot.
I'm going to type plt.xlabel.
And we'll just put it in an X for the x-axis.
And we can use the same idea for ylabel, in which case we'll just call it Y.
If you're familiar with LaTeX, which is the typesetting software often used
in mathematical publications, you'll be pleased to know
that plt also knows LaTeX.
If you're not familiar with it, here's a brief idea.
We can take a mathematical notation or a symbol like x,
and we can put dollar signs around that.
All this does is that it changes the appearance of x and y in your plot.
Let's try running the plot up to this point.
If you're not familiar with LaTeX, you can drop the dollar signs
and we can re-run the code to see what changes.
Pay close attention to the axes labels.
The axes labels are still x and y, but the specific appearance of the font
looks a little bit different.
Let's then use axis function to adjust the axes.
So I'm going to type plt.axis parentheses
and inside goes a list.
The first argument is going to be xmin.
The second one is xmax.
The third one is ymin.
And the fourth one is ymax.
xmin specifies where the x-axis starts in my plot.
I'm going to use the number minus 0.5.
xmax, I'm going to use 10.5
so I'm going to be going a little bit over the length of my x vector.
For ymin, I'm going to be using minus 5.
And for ymax, I'm going to be using 105.
Let's try re-running this and see how it changes in a subtle way
the appearance of the plot.
You see that the axes have now been adjusted.
Let's then add a legend to our plot.
There are two steps.
The first step is to give labels.
I'm going to say a label equal to, let's just called this First,
you'll see that the label is going to be a string.
I also want to give a label for my second plot.
I'm just going to call that Second.
To show the legend, I have to type plt.legend.
And I can use an additional keyword argument, loc for location,
to specify the specific location of the legend.
In this case I would like to use the upper left corner for my legend,
and we can try running the code,
and we'll see that the legend appears in the upper left corner.
Finally, we'd like to be able to save our figure to file.
To do that, we'll use the savefig function,
and inside the parentheses goes the name of my plot.
I'm just going to call that myplot.
I'd like this to be a pdf plot
so I'll just enter the pdf file extension here.
I'm going to run this code
and Python will now have created a plot called
"myplot.pdf" in the working directory.
The working directory is the directory where you have launched your Python.
Let's see if we can find the plot that we just created.
I'm going to launch finder.
I know the name of my plot is myplot.pdf.
And we can see that this plot has just been created.
I can double click that to open my pdf.
In this case, my plot is beautifully stored in a pdf file.




'''

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,20,21)
y1=x**2
y2=x**1.5

print(x,y1)
plt.plot(x,y1,"gs-",linewidth=2,markersize=4,label="First")#gs is green squares
plt.plot(x,y2,"rd-",linewidth=2,markersize=4,label="Second")
plt.legend(loc="upper left")#to  diplay the labels of the plot
plt.xlabel("$X$")#dollor gives an italian look
plt.ylabel("$Y$")
plt.axis([.5,30,-50,400])#Limit the window axes
# plt.axis([xmin,xmax,ymin,ymax])
plt.savefig("myplot.png")# to save the figure
#print(p)
plt.show()

