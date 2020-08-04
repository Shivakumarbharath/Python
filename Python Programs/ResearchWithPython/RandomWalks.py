'''

tart of transcript. Skip to the end.
This is a good point to introduce random walks.
Random walks have many uses.
They can be used to model random movements of molecules,
but they can also be used to model spatial trajectories of people,
the kind we might be able to measure using GPS or similar technologies.
There are many different kinds of random walks, and properties of random walks
are central to many areas in physics and mathematics.
Let's look at a very basic type of random walk on the white board.
We're first going to set up a coordinate system.
Let's call this axis "y" and this "x".
We'd like to have the random walk start from the origin.
So this is position 1 for the random walk.
To get the position of the random walker at time 1, we can pick a step size.
In this case, I'm just going to randomly draw an arrow.
And this gives us the location of the random walker at time 1.
So this point here is time is equal to 0.
And this point here corresponds to time equal to 1.
We can take another step.
Perhaps in this case, we go down, say over here.
And this is our location for the random walker at time t is equal to 2.
This is the basic idea behind all random walks.
You have some location at time t, and from that location
you take a step in a random direction and that generates your location
at time t plus 1.
Let's look at these a little bit more mathematically.
First, we're going to start with the location of the random walk at time t
is equal to 0.
So position x at time t is equal to 0 is whatever
the location of the random walker is at the beginning of the random walk.
We're going to call that x0.
These are step 0.
The next step is going to be the location of the random walker at time t
is equal to 1.
This will be given to us by the location of the random walk at the previous time
step, t is equal to 0, plus some displacement, delta x,
at time t equal to 1.
Because x at t0 is simply given by this term over here,
we can simplify this to x0 plus delta x at time t equal to 1.
Let's then look at the next step.
The location of the random walker at time t is equal to 2.
Again, the basic idea is the same.
The new location is going to be the old location, meaning x at time t
is equal to 1 plus some random displacement delta x at time t
is equal to 2.
Note that the index of the random displacement
matches the index of time over here.
From what we have above, we see that we have the location at time t equal to 1
here, which we know to be equal to this term over here.
What that means, I can now rewrite this part as this expression here.
So we have x0 plus delta x at time t equal to 1 plus delta x at t
equal to 2.
This term over here is just the same term that we had above here.
All we've done is we've just copied that term over here.
We can see that a common pattern starts to emerge.
To note the location of the random walker at time 2,
we had the initial location plus displacement at time t equal to 1
and t equal to 2.
From this we can write down the general equation
for the location of the random walk.
We start with x at some point in time, t is equal to k, for example.
We will always have the initial location x0,
and this is going to be followed by a sum of displacements.
The first displacement is going to be this term delta x at time t equal to 1.
This will be added to the displacement delta x at t equal to 2 all the way
to displacement delta x that corresponds to t equal to k.
In other words, the location of the random walker at any point in time
is given by the initial location x0 plus the sum of all of the displacements
from 1 to k.
Let's review the logic of the argument here.
First we start at time t is equal to 0, which
we decided we're going to call x0.
Then at time t equals 1, we take the previous location
that we had at time t equal to 0, and then we
add a random displacement to that.
That gives us location at time is equal to 1.
I'm going to use the blue color for this.
Then when we look at the location of the random walker at time t is equal to 2,
we take the location at t is equal to 1 as a starting point.
Again we add the random displacement.
The final result is the following.
To find out the location of the random walker at time t
is equal to k, we take the initial locations of the random walk,
and to that we add a sequence of random displacements.
If we're interested in the location after k steps,
then we will have k such random displacements in the sum.
We've just seen that the location of the random walker, at any given time t,
is given by a cumulative sum of the previous t displacements
leading up to that point.
Let's try coding up random walker in NumPy, where we start at the origin,
take 100 steps, and where each step is sampled
from the standard normal distribution.
The normal distribution having mean 0 and standard deviation equal to 1.
We're also going to assume that the x displacement and the y
displacement for any given step are independent, such
that the displacement in the horizontal direction
has nothing to do with the displacement in the vertical direction.
We can start by generating the displacements.
I'm again going to keep the numbers small and started with just five steps.
Let's generate a two by five table of numbers for each element,
each of the 10 numbers is drawn independently
from a standard normal distribution.
To do this, we will use the np.random.normal function.
In this case, we'll be typing np.random.normal.
The first argument is the location or the mean.
The second one is the standard deviation, which is 1.
And we wanted to generate a two by five table, two rows and five columns.
And we can try running this a couple of times
to see that the dimension of the table matches what the expectation was.
I'm going to call this table delta x, because this encodes
the displacements of the random walker.
So delta x equals np.random.normal.
Let's then pull up these displacements.
We can take the first component of each vector
as the x-coordinate and the second component as the y coordinate.
We're going to be using plt plot for this.
So we'll say plt.plot.
We'll be taking the delta x array.
We would like to get row 0 from that array.
That's our x component.
And our y component, the second argument of the plot function,
is going to be delta x1, which is row one of delta x.
Then as the third argument, I can specify the color and marker.
I like to be using green circles for this plot.
And then we run the code.
What is shown here are the displacements that we
generated from the normal distribution.
It may seem like we're just getting started with this example,
but in fact we're almost done.
The one missing piece that we need is what is called a cumulative sum.
Let's first look at what that means.
Let's have some numbers-- 2, 4, 1, 3, and 2.
Underneath we'll write the cumulative sum.
The first element is just going to be equal to 2, the first element here.
The next element is going to be whatever we had here plus the element above.
2 plus 4 gives us 6.
This element is going to be 6 plus 1, that's 7.
7 plus 3, that's 10.
10 plus 2, that's 12.
But how can we do a cumulative sum in NumPy?
Let's just Google that to find out.
Cumulative sum in NumPy.
In this case the first hit gives us what we would like.
NumPy has a function called cumulative sum,
and it requires at least one argument.
In this case the function requires one compulsory argument, which
is an array, in this case called a.
The second argument, axis, which is optional,
specifies the axis along which the cumulative sum will be computed.
Let's practice the use of the cumulative sum.
np.cumsum.
It's going to be applied to delta x, which is the first argument.
And the second argument specifies the axis.
We're going to be using axis equals 1 because we
would like to take the cumulative sum over the columns of this array.
I would like to store this result. I'm going
to store that in X-- that's capital X. And if we
look at the contents of the array, we will
see that we now have a cumulative sum taking over the columns.
We can contrast this with delta x, which only gives us the increments that we
sampled from the normal distribution.
Let's now put the different pieces together.
First we generate the random displacements, np.random.normal,
mean 0, standard deviation 1.
And the size of the array is two by five.
This gives us our delta x, our random placements.
On the following line we'd like to define
x, which is the position of the random walker at any given time.
So we apply the cumulative sum here, applied to delta x,
and axis being set to 1.
Finally, we want to plot this using plt plot.
First we'll plot the row 0 of our X array
and then we plot row 1 of the array.
Let's try running the code.
Let's try making a small modification to the plot.
I would like to be using red circular markers,
and I would like them to be connected with straight lines.
I would then like to save this figure.
So I'm going to be using this Savefig command.
And I'm just going to call this rw, short for random walk.
And I'd like that to be a PDF file.
I will then run the code.
And let's look for the PDF file on my computer.
This shows us the first four steps of the random walk,
but there is one problem here.
Remember how the random walk was supposed to start at the origin,
at location is 0,0?
Right now we're missing that very first point.
But let's add that element to our array.
In this case the origin is represented by a two by one array consisting of 0s.
And we'd like to concatenate that to our array called X. Let's again use Google
to find out how to do that.
How to concatenate NumPy arrays?
Again, the first hit looks promising.
In this case we need to provide two arguments.
The first argument is a tuple of the arrays
that we would like to concatenate.
The second argument, axis, is the axis along which the arrays will be joined.
So the missing step for us to do is to generate the array X_0.
And we know that this is an NumPy array.
It consists of two rows, each having just one element, 0.
These array X_0 gives us the initial location of the random walker.
Let me take this line of code and move the top here in my window above.
And we can now write the concatenation function.
We start with np.concatenate and we need to provide two arguments.
First is a tuple of the arrays that we would like to concatenate.
And a second argument, axis, specifies the dimension of concatenation.
In this case, axis is going to be equal to 1.
Let's now look at the tuple argument a little bit more carefully.
The first array is going to be X0, the starting point of the random walk.
For the second argument, we will need to insert our cumulative sum from above.
So this is the cumulative sum applied over delta x along axis 1.
This entire expression here will give us the location
of the random walker, which is x, this time including
the origin as the starting point of the walk.
We can now inspect the array X. And we'll see that the first element is 0.
We are now ready for our final solution.
Let's first copy this bit of code from here.
This replaces our previous definition of X. So we now define X0,
we generate our delta x's, we then define
X the location of the random walk, and we then make the plot.
Finally, we'll save the figure.
I'm going to save the figure now to a file called rw2
and we can run the code.
Let's again look at the PDF version of the plot that we just generated.
We're looking for rw2.
And we can see that this time the random walk does start at the location 0,0,
at the bottom of the figure.
Let's now run this 100 times.
We're going to change the argument here that specifies
how many random displacements I would like to generate from my random walker.
I'm going to save this in file rw3
and then we'll run the code.
We can look at the file,
searching for rw3,
and this is our random walker which takes, in this case, 100 steps.
To wrap this up, let's generate a couple of realizations of random walk
taking 10,000 steps.



'''

import numpy as np
import matplotlib.pyplot as plt

delta_x = np.random.normal(0, 1, (2, 1000))  # (location,standerd deviation,table
print(delta_x)
# plt.plot(delta_x[0],delta_x[1],'go')
# plt.show()

# cumilative sum
x_cumsum = np.cumsum(delta_x, axis=1)
print(x_cumsum)
# plt.plot(x_cumsum[0],x_cumsum[1],'yd-')
# plt.show()

# after concatination

x_0 = np.array([[0], [0]])
y = np.concatenate((x_0, x_cumsum), axis=1)  # starts at zero
plt.plot(y[0], y[1], "bs-")
plt.show()
