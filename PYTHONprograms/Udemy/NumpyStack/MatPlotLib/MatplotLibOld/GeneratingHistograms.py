'''

rt of transcript. Skip to the end.
There are many ways to generate histograms.
Let's look at one of them, which is using the hist function from the plt
library.
To get started, let's first generate some random numbers.
In this case, we'll use the np random normal function
to generate 1,000 samples or draws from the standard normal distribution, which
is a special case of the normal distribution that has mean equal to 0
and variance equal to 1.
Let me first import the matplotlib.pyplot library as plt.
And then I'm also going to import the NumPy library.
The first step is going to be to create random numbers.
Here we'll be using np.random.normal.
And I need to specify how many numbers I'd
like to draw from the standard normal distribution.
In this case, I'd like to have 1,000 numbers.
And I will assign this array into a vector x.
We'll then call the plt.hist function.
And Python returns a histogram to us.
There are many optional parameters in the hist function.
And the best way to get to know them is to explore online documentation.
You can just Google plt hist, and you'll get many hits.
To demonstrate some of the features of hist,
I'll show how to normalize the histogram and how
to provide locations of bin edges that are used to construct the histogram.
By default, hist uses 10 evenly spaced bins
and it tries to optimize both bin width and bin locations.
But sometimes you really want to be able to specify the bins yourself.
Let's go back to our previous example where
we had generated 1,000 random variables from the standard normal distribution.
We'll continue working with our plt.hist example,
except that we will add first one extra argument, which is normed.
When we set normed to be true, the histogram, in this case on the y-axis,
instead of having the number of observations that fall in each bin,
we have the proportion of observations that fall in each bin.
That's what it means for a histogram to be normalized.
To provide the location of the bins, we used a keyword argument called bins.
I'm going to construct the bins using the np.linspace function.
Remember, the first argument is the starting point.
I'm going to start at 5, minus 5.
I want to go all the way to plus 5.
And I'd like to have 21 points.
In this case, you see that the histogram looks different.
That's because we have specified 20 bins between the numbers minus 5 and plus 5.
In the previous example, we generated 21 points to get 20 bins.
Let's make sure we understand why.
If we think about the first example where we just
have one bin, to have one bin we need to specify
the start point-- the start location of the bin
and the end location of that bin.
So to get one bin, we need two points.
If we had two bins we would need three points, and so on.
This is why to have 20 bins, we will need to have 20 plus 1,
or 21, points along the x-axis.
Let's then examine another distribution, which is a bit more exotic,
the so-called gamma distribution.
It is a continuous probability density function that starts at 0
and goes all the way to positive infinity.
The gamma distribution, like the normal distribution, has two parameters.
For now, we don't need to be too concerned about the nature of the gamma
distribution.
We just know that it's some type of probability distribution,
and we'd like to investigate its shape using histograms.
In this case, we're going to draw a large number of samples
from the gamma distribution.
Let's go with 100,000 samples which would give us a very smooth histogram.
We'll also meet here a plt function called
subplot, which enables us to have several subplots within each figure.
This upload function takes in three arguments where the first two specify
the number of rows and the number of columns in the subplot,
and the third argument gives the plot number.
For example, if you specify two rows and three columns,
then you will have six subplots.
The plot number always starts at 1, so in a two by three subplot,
the plot numbers range from 1 to 6, where the plot numbers
are incremented across rows first.
Let's see how this works.
Let's look at a two by three subplot.
In this case, we have two rows and three columns.
So this would be a two by three subplot.
The first panel in the top left corner is subplot number 1.
This is number 2.
And this is number 3.
Then we move on to the next row.
We have number 4, number 5, and number 6.
Let's first draw our samples from the gamma distribution.
I'm going to call my variable "x".
We're using the random.gamma function.
The first two arguments are 2 and 3.
And the third one specifies that we would
like to have 100,000 samples from this specific gamma distribution.
To learn about the different histogram options,
we have the code up here that demonstrates four different ways
of drawing a histogram.
I'll walk you through now each one of them.
We'll then in the end create one plot that consists of four subplots
to demonstrate the use of the subplot function.
First, we'll just use the plt hist function.
We'll provide x, our input vector, and we specify the number
of bins, which in this case is 30.
And this is what the histogram looks like.
If we'd like to normalize this histogram,
we can use the keyword argument normed, and we set that to be equal to true.
In this case, the histogram will be normalized.
We can also try looking at the cumulative histogram.
So we'll say cumulative equals true.
And in this case, we get the cumulative histogram.
We can also have both normed and cumulative options be on
at the same time.
In this case, I can just add normed equals true.
And I can also change the histogram type.
I can do that by using the hist type keyword argument.
And I'd like to use a step histogram here.
And this is the output that I get.
We can now pool all of these four different histograms into one figure.
I will first create a figure by saying plt.figure.
And I then insert each of these histograms into its own subplot.
Let's see what happens.
In this case, we have created just one figure
with four panels where each type of histogram appears in its own subplot.



'''


import matplotlib.pyplot as plt

import numpy as np

x=np.random.normal(size=1000)

plt.hist(x,bins=np.linspace(-5,5,20))

plt.show()