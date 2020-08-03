'''


art of transcript. Skip to the end.
It is often helpful to be able to measure how long a segment of code
takes to run.
One reason for wanting to know might be that you
have two or more ways of coding up the same task
and you'd like to know which one is faster.
Another reason might be that you have a large dataset
and you'd like to have a sense ahead of time
how long it might take to run your code.
You could do this by running the code for smaller datasets first, time the
running time, and then extrapolate from there to the running
time for the whole dataset.
A simple way to measure time in Python is to use the time module.
We will import the module by saying import time.
One of the most useful functions in the time module is the time.clock function.
That gives us the current time.
We can capture that in a variable called start time.
So we just type start_time equals time.clock.
And then we can run this again to extract the end time.
I'm going to call that end time.
So end_time equals time.clock.
If I want to see how much time has elapsed between these two time points,
I can take my end time and from that, I will subtract my start time.
There are a few different ways to measure time in Python and each of them
has its uses.
But for many purposes, such as comparing performance,
time.clock is the right function to use.
Working with our previous example, the one that relied only on pure Python,
I have the code here in front of me.
In order to time its performance, I'm first
going to catch the start time by saying start_time equals time.clock.
The code will run
and once it's finished, I went to capture the end time.
So I capture time here again.
And then what I'd like to do is print the difference between end time
and start time.
Let's try running this code.
In this case, we might expect this to take somewhere between 5 seconds
and perhaps up to 1 minute, depending on the speed of your computer.
Let's then look at the second implementations of this example,
the one that relies on NumPy.
Again, we will capture start time,
and will the same once the code has run.
In this case, we just have two lines for the code.
And in the end, we just want to print out the difference between end time
and start time.
We would expect this code to run much faster because it makes use of NumPy.
In this case, the code runs almost immediately.
Let's look at the difference in performance
between these two different ways of implementing the same example.
I'm going to take the time I got from the first example, the pure Python
implementation, and I will then divide that by the time I got using NumPy.
In this case, we see that the NumPy implementation is over 80 times faster
than the Python-based implementation.



'''

import time
import matplotlib.pyplot as plt
import numpy as np

start_time = time.time()
# code
x = np.random.randint(1, 7, (100, 10))

y = np.sum(x, axis=1)
plt.hist(y)
plt.show()

end_time = time.time()
print(end_time - start_time)
