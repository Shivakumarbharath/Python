'''


It's easy to index and slice NumPy arrays regardless of their dimension,
meaning whether they are vectors or matrices.
With one-dimension arrays, we can index a given element
by its position, keeping in mind that indices start at 0.
With two-dimensional arrays, the first index
specifies the row of the array and the second index
specifies the column of the array.
This is exactly the way we would index elements of a matrix in linear algebra.
We can also slice NumPy arrays.
Remember the indexing logic.
Start index is included but stop index is not,
meaning that Python stops before it hits the stop index.
NumPy arrays can have more dimensions than one of two.
For example, you could have three or four dimensional arrays.
With multi-dimensional arrays, you can use the colon character
in place of a fixed value for an index, which
means that the array elements corresponding
to all values of that particular index will be returned.
For a two-dimensional array, using just one index
returns the given row which is consistent with the construction of 2D
arrays as lists of lists, where the inner lists correspond
to the rows of the array.
Let's then do some practice.
I'm first going to define two one-dimensional arrays,
called lower case x and lower case y.
And I'm also going to define two two-dimensional arrays,
and I'm going to denote them with capital X
and capital Y. Let's first see how we would
access a single element of the array.
So just typing x square bracket 2 gives me the element located at position
2 of x.
I can also do slicing.
So I can specify the start index and the end index, in which case
I get two elements here from the x array, the numbers 1 and 2.
If you look at the sizes of x and y, each of them
has exactly three elements.
That means that we can add those two arrays up.
So I can type x plus y, which gives me a new array called z.
In this case, the elements of z will be element-wise additions
from the vectors x and y.
So the first element of x is added to the first element of y, and so on.
Now moving on to two-dimensional arrays,
we can also investigate individual rows or columns of arrays.
Typing X square bracket colon comma 1 gives me
access to the first column of the table X. I can do the same for Y,
and now I have to first column of the two-dimensional array, Y.
I can also add these two up.
So I can type X plus Y, again colon comma 1.
In this case, I have added together the first columns of these two arrays.
To extract the first row of X, I type, within square brackets,
1 comma colon which gives me all of the elements in the first row.
In this case, these are numbers 4, 5, and 6.
I can take also the first row of Y, and I can then add these two arrays up.
Because two-dimensional arrays are defined as nested rows,
I can use a shorthand notation to access the first row of X, which in this case
would be just X square brackets 1, and this gives me the same exact output
as typing X square bracket 1 comma colon.
One word of caution --
what happens if we take two lists and put a plus sign between them?
Well, we can give it a try.
I can define a list which consists of elements 2 and 4.
I have a plus sign followed by another list with elements 6 and 8.
Remember, putting a plus sign between two lists
concatenates those two lists, resulting in a new list which is longer than
the two lists that were added together.
Now let's look at a different example.
What happens if we first turn those lists into NumPy arrays,
and then have a plus sign between them?
I'm going to take my previous line here.
I'll just turn this into a NumPy array.
So my first NumPy array has two elements, 2 and 4.
I'm going to add that to another NumPy array, which has elements 6 and 8.
In this case, what's happening is we have two one-dimensional arrays.
And what we've accomplished here is an element-wise addition
between these two arrays.


'''

import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])

X = np.array([[1, 2, 3],[8,5,6]])
Y = np.array([[4, 5, 6],[9,5,1]])

print(x[2])
print(x[0:2])
z=x+y
print(z)
print(X[:,1])#acess the 1st column
print(X[1])#acess the first row

print(X[1,1])#access by row,column