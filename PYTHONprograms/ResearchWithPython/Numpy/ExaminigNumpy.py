'''


NumPy provides a couple of ways to construct arrays with fixed,
start, and end values, such that the other elements are uniformly
spaced between them.
To construct an array of 10 linearly spaced elements starting with 0
and ending with 100, we can use the NumPy linspace function.
In this case, I'm going to type np.linspace.
The first argument is the starting point, which is 0.
The second is the ending point, which will be included
in the NumPy array that gets generated.
And the final argument is the number of points
I would like to have in my array.
In this case, NumPy has created a linearly spaced array starting at 0
and ending at 100.
Now, to construct an average of 10 logarithmically spaced elements
between 10 and 100, we can do the following.
In this case we use the NumPy logspace command.
But now careful, the first argument that goes into logspace
is going to be the log of the starting point.
If you want the sequence to start at 10, the first argument
has to be the log of 10 which is 1.
The second argument is the endpoint of the array, which is 100.
And again, we need to put in the log of that, which is 2.
And the third argument as before, is the number of elements in our array.
in this case, what NumPy has constructed is an array consisting of 10 elements
where the first element is 10 and the last element is 100.
All of the other elements are uniformly spaced between those two extreme points
in the logarithmic space.
To construct array of ten logarithmically spaced elements
between numbers say 250 and 500, we first
need to take the base 10 logarithm of the numbers, 250 and 500,
and then feed those into the logspace function.
So let's try that out.
I'm going to start by typing np.logspace.
And now we need to take the base 10 logarithm of the number 250.
To do that, I will type np.log10 and the number is 250.
For the second argument, I'm again going to be taking the logarithm base
10, in this case of the number 500, and I would
like to have 10 elements in my array.
When I run this, the output is exactly what's expected.
Often we need to know the shape of an array
or the number of elements in an array.
You can check the shape of an array using shape.
I'm going to define the two dimensional array x,
and to find out the shape of the array I can type x.shape.
You can check the number of elements of an array with size.
So in this case, I can type x.size and I find out
that I have six elements in my array.
Notice that you don't have parentheses following the shape
or size in the above examples.
This is because shape and size are data attributes, not methods of the arrays.
Sometimes we need to examine whether any or all elements of an array
fulfill some logical condition.
Let's generate a small one d array and check two things.
First, if any of the entries are greater than 0.9,
and second, if all of the entries are greater than or equal to 0.1.
You may remember how we generated random numbers using the random module.
NumPy has its own random module.
And in this case, we're going to be generating 10 random numbers drawn
from the standard uniform distribution, meaning from the interval from 0 to 1.
I'm going to call this vector or array "x".
And now we can use the np.any function to find out if any of the elements of x
are greater than 0.9.
And the answer is this case true.
I can then use the np.all function to find out
if all of the elements in the array are greater than or equal to 0.1.
In this case, the answer is true.
To make sense of these results, we can print out the content of x.
By looking at the second element on the second row, which
is to 0.9216 and so on, we have an element which is greater than 0.9.
Therefore, we have at least one of those elements,
and therefore np.any returns true to us.
If you look at all of the elements in our vector x, you see that all of them
are indeed greater than 0.1.
And that's why np.all also returns true.
Note that the output is either true or false for the whole array.
Either there is or is not one or more entries that are greater than 0.9.
Also, either all entries are greater or equal to 0.1 or they are not.
This is why the output is just a single true or false.



'''

import numpy as np

y=np.linspace(0,100,11)
print(y)

j=np.logspace(1,2,3)
print(j)



k=np.logspace(np.log10(250),np.log10(500),7)
print(k)

'''
Sometimes we need to examine whether any or all elements of an array
fulfill some logical condition.
Let's generate a small one d array and check two things.
'''

ran=np.random.random(10)

print(ran)

print(np.any(ran<0.9 ))

print(np.all(ran>=0.1))



























