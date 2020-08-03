'''


NumPy is a Python module designed for scientific computation.
NumPy has several very useful features.
Here are some examples.
NumPy arrays are n-dimensional array objects
and they are a core component of scientific and numerical computation
in Python.
NumPy also provides tools for integrating your code with existing C,
C++, and Fortran code.
NumPy also provides many useful tools to help
you perform linear algebra, generate random numbers, and much, much more.
You can learn more about NumPy from the website numpy.org.
NumPy arrays are an additional data type provided by NumPy,
and they are used for representing vectors and matrices.
Unlike dynamically growing Python lists, NumPy arrays
have a size that is fixed when they are constructed.
Elements of NumPy arrays are also all of the same data
type leading to more efficient and simpler code
than using Python's standard data types.
By default, the elements are floating point numbers.
Let's start by constructing an empty vector and an empty matrix.
By the way, don't worry if you're not that familiar with matrices.
You can just think of them as two-dimensional tables.
We will always use the following way to import NumPy
into Python-- import numpy as np.
This is the import we will always use.
We're first going to define our first zero vector
using the numpy np.zeros function.
In this case, if we would like to have five elements in the vector,
we can just type np.zeros and place the number 5 inside the parentheses.
We can define a two-dimensional array-- let's
called that zero_matrix-- in the following way:
We, again, provide only one argument to NumPy.
In this case, it has to be a tuple.
A tuple specifies two things.
The first argument is the number of rows in the table
and the second argument is the number of columns in our table.
So if you would like to create a five by three table,
we type np.zeros, two parentheses, 5 comma 3, and two closing parentheses.
Both the zero_vector and the zero_matrix will contain only zeroes
as their elements.
We can see it as we type zero_vector, and similarly if we type zero_matrix.
You can also construct arrays of ones using the np.ones function,
and its index is identical to the syntax of the zero's function.
To create an empty array, you can use the np.empty function, which
allocates the requested space for the array, but does not initialize it,
meaning that the content could be anything, whatever
happens to be in the computer's memory at the location where
the array is set up.
If you are dealing with a very large array
and you know for sure that you will be updating each element of the array,
this could save you some computation time
because Python doesn't need to initialize the array.
However, you should use this function with care
and if you're new to NumPy, it's probably best to avoid it at first.
We can also construct NumPy arrays using specified values, in which case,
we use the np.array function, and the input argument to the function
is a sequence of numbers, typically a list of numbers.
In what follows, we assume that lower case variables
are vectors or one-dimensional arrays and upper case variables are
matrices, or two-dimensional arrays.
To practice creating NumPy arrays, let's create
two, short, one-dimensional arrays.
Our first array is going to be called x, and it
consists of the numbers 1, 2, and 3.
Our second NumPy array is going to be called y,
and that's going to consist of the numbers 2, 4, and 6.
When you construct a two-dimensional NumPy array,
you specify the elements of each row as a list
and you can then define the entire table as a list that contains at its elements
each of the lists of the row elements you've defined.
Let's work through a simple example.
Let's define the first row as consisting of numbers 1 and 3.
Then we can define the second row as consisting of the numbers 5 and 9.
So here we have two lists that are separated by a comma.
And we will embed these two lists inside yet another list,
and now we have our nested list object.
To turn this into a NumPy array, we type np.array and the nested list object
goes inside the parentheses.
Finally, sometimes you want to turn the table sideways.
This is called taking the transpose of a matrix, which
means that the first row becomes the first column,
the second row becomes the second column, and so on.
Notice that another identical way to state this
is to say that the first column becomes the first row.
The second column becomes the second row, and so on.
We can transpose a two-dimensional array using the transpose method.
If we go back to the array that we had here-- let's call this A.
We can use now the transpose method to flip the array around.



'''

import numpy as np

zero_vector = np.zeros(5)

zero_matrix = np.zeros((5, 3))

print(zero_vector)

print(zero_matrix)

a = np.array([[1, 2, 3], [6, 5, 4]])
print(a)

print(a.transpose())
