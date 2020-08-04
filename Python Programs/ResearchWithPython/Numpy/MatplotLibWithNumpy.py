'''

tart of transcript. Skip to the end.
NumPy makes it possible to generate all kinds of random variables.
We'll explore just a couple of them to get you
familiar with the NumPy random module.
The reason for using NumPy to deal with random variables
is that first, it has a broad range of different kinds of random variables.
And second, it's also very fast.
Let's start with generating numbers from the standard uniform distribution,
which is a the completely flat distribution between 0
and 1 such that any floating point number between these two endpoints
is equally likely.
We will first important NumPy as np as usual.
To generate just one realization from this distribution,
we'll type np dot random dot random.
And this enables us to generate one realization
from the 0 1 uniform distribution.
We can use the same function to generate multiple realizations
or an array of random numbers from the same distribution.
If I wanted to generate a 1d array of numbers,
I will simply insert the size of that array, say 5 in this case.
And that would generate five random numbers drawn
from the 0 1 uniform distribution.
It's also possible to use the same function to generate
a 2d array of random numbers.
In this case, inside the parentheses we need to insert as a tuple
the dimensions of that array.
The first argument is the number of rows,
and the second argument is the number of columns.
In this case, we have generated a table --
a 2d table of random numbers with five rows and three columns.
Let's then look at the normal distribution.
It requires the mean and the standard deviation as its input parameters.
In this case, I'd like to set the mean to be equal to 0,
and standard deviation equal to 1.
This gives us the so-called standard normal distribution.
Just to be clear, there are an endless number of different distributions
depending on the parameter values.
But only the one with mean equal to 0 and a standard deviation
equal 1 one has its own name-- the standard normal distribution.
To generate random numbers from the standard normal distribution,
or from the normal distribution in general,
we will be using the np dot random dot normal function.
The first argument is the mean of the distribution, in this case 0.
And the second argument is the standard deviation, which is equal to 1.
Using this syntax enables us to draw one realization, one number,
from the standard normal distribution.
If we'd like to generate instead a 1d array of numbers
from the same distribution, we can specify the length of the 1d array
as the third argument.
In this case, if I would like to generate an array of five numbers,
I will simply add a third argument, which is number 5 in this case.
Finally, we can use the same function to generate 2d, or even
3d arrays of random numbers.
In that case, we need to insert another pair of parentheses
because the dimensions of the array will be added as a tuple.
If I'd like to generate a 2d array consisting
of two rows and five columns -- those arguments go right inside the tuple,
and I can still continue to use the same function.
Let's revisit our example where we roll 10 die and added the result together.
Remember, we defined a random variable y as the sum of random variables x1
through x10, where each x variable is a standard
die with 6 faces with the numbers from 1 to 6 on them.
We can code this example using NumPy arrays.
My overall strategy is to generate a table
where each element corresponds to a roll of a die such
that each element is a number between 1 and 6.
If I have 10 columns in my table, I can then create my variable y
by summing the table over all columns.
Finally, the number of rows in the table is
going to be equal to the number of realizations of the variable y
that I would like to generate.
Let's look at this on the white board.
I'm going to generate a small table in this case
with just three columns and four rows.
The first column is x1,
the second column is x2, all the way to the last column, which is x10.
My rows in the table would then correspond to different realizations
of the variable y.
So for example, my first realization of y
is called a y1, would be the sum over the 10 different columns of the table.
My second realization of y would be a sum across the second row
and over all of the 10 columns of the table.
The only problem is that we don't know how to generate
an area of random integers in NumPy.
Let's Google it.
The first hit is NumPy.random.randint.
That looks promising
so let's take a closer look at the help page.
This function looks promising.
If you look at the input arguments, we have to provide at least one argument
but we can potentially provide up to three different arguments.
Let's try out this function.
I'm going to type np.random.ranint.
I will generate just one realization.
And the function seems to be working fine.
When dealing with relatively large amounts of data, such as large arrays,
it's very helpful to start small when writing your code.
Starting small keeps things much more manageable
and the fact that you can look at the data on the screen
makes it much easier to locate potential problems.
Instead of having 10 columns, I'm just going
to be using three columns for now.
Also, instead of having 100 or 1 million rows,
I'm just going to go with just 10 rows.
Let's generate this random array in NumPy.
I'm going to call this variable capital X. We'll type np.random.randint.
We'll use the same start and end points, except that in this case
we need to provide a third argument, which is the size of the array.
We would like to have 10 rows and 3 columns.
If we now look at the variable x, we see that it has 10 rows and 3 columns.
We can also check the shape of the array by using
the shape function x dot shape.
Python tells us x has 10 rows and 3 columns.
The next step would be to sum over all rows of x.
NumPy has a function called sum
but I'm not fully sure how to use it,
so let's look at the documentation.
We could also Google this
but in this case, I'm going to be using the command line help in iPython.
To do that, I'm going to be typing np.sum.
And Python returns to me information about the np sum function.
Scrolling to the top of the page, I see that only one argument, a,
is necessary, which is the array of elements.
The second optional argument is called axis.
When using two dimensional or higher dimensional arrays,
we need to specify the dimension on which the sum is taken.
Let's practice using the NumPy sum function.
If we type np.sum, we get a sum over all of the elements of the array.
We can also specify the axis or dimension along which
we would like to take a sum.
We can also provide the optional argument axis, in this case equal to 0,
in which case we are summing over all of the rows of the array.
We can also try summing over dimension 1, in which case
we're summing over all of the columns.
If we had a three-dimensional array, to sum over the third dimension,
we could set the argument axis equal to 2.
In this case, when I run this, Python gives me the error message--
axis entry is out of bounds.
This is because I'm trying to sum over axis dimension 2,
whereas I only have two dimensions -- dimensions 0 and 1.
Summarizing our finding, taking a sum over dimension 0 sums over rows,
and taking a sum over dimension 1 sums over columns.
So I'm now ready to write my y variable.
I'm going to define y as np sum of x over axis equals 1.
If I now inspect my variable y, I'll see that it has 10 elements as expected.
Let's now put our code together.
The first line is going to be, again, random.randint 1 comma 7.
And I will now insert the actual dimensions of the array --
100 rows and 10 columns.
My y variable is going to be formed as a sum
so I'm using np sum of x.
And here I specify axis equal to 1, which is dimension 1 of the array.
If you wanted to plot the histogram of this, we can just say plt.hist of y.
Let's try running this code.
In this case, we see that Python plots a histogram, which looks very
similar to the histogram we saw before.
But let's see what happens as we increase
the number of rows in our table.
I'm going to go back to my code and modify the 100 to 10,000.
I will also put a semi-colon at the end of plt.hist
to suppress the output of the histogram function.
And we can see that the histogram looks smoother.
I can further increase the size of the table to 1 million.
Remember, in this case we're generating 1 million realizations of variable y.
And the histogram looks even more smooth in this case.
You can see that this code is shorter than our previous code
for the same example that didn't make use of NumPy.
Another difference you probably noticed is that this code is much faster.
Generally, using NumPy can result in code
that runs over 10 times faster than standard Python code.
In scientific computation, this makes a big difference.


'''

import numpy as np
import matplotlib.pyplot as plt

'''
print(np.random.random(5))
print(np.random.random((2,3)))

output

[0.39147332 0.88381278 0.40368459 0.76730572 0.79610452]
[[0.24848792 0.491144   0.29463463]
 [0.12706984 0.89152377 0.42209408]]



print(np.random.normal(0,1,5))to make two d put() instead of 5
[ 0.47025106 -0.09488634  0.64112434  0.28091327  0.21086202]

'''

x = np.random.randint(1, 7, (10, 3))
print(x.shape)
print(x)
print(np.sum(x, axis=1))  # axis 0 is 1d and 1 is 2d d

y = np.sum(x, axis=1)
plt.hist(y)
plt.show()
