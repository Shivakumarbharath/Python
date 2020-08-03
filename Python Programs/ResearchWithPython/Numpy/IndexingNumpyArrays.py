'''


NumPy arrays can also be indexed with other arrays
or other sequence-like objects like lists.
Let's take a look at a few examples.
I'm first going to define my array z1.
And let's put in a few elements in there-- 1, 3, 5, 7, and 9, for example.
I can then define a new array called z2, which is just z1 with one
added to every single element of the array.
We can now look at these two arrays to see what their contents are.
I can now define a list called n, which I will be using to index my z1 and z2.
So let me put in the elements 0, 2 and 3 in my index.
I can now type z1, square bracket, ind, which gives me access
to the elements that are located within z1 at the locations that
are specified by ind.
In this example, index or ind, was defined as a Python list,
but we could also have defined that as a NumPy array.
So I can take my previous list, 0, 2, 3, turn that into a NumPy array,
and I can still do my indexing.
In other words, we can index NumPy arrays
using either lists or other NumPy arrays.
NumPy arrays can also be indexed using logical indices,
but what does that actually mean?
Just as we can have an array of numbers, we
can have an array consisting of true and false, which are two Boolean elements.
Let's first construct a Boolean array.
I'm going to define my z1 again here as before.
I can now type something like z1 greater than 6.
The element 0 of z1 is not greater than 6,
and therefore element 0 of the Boolean array that Python returns to you
is false.
The same is true for elements 1 and 2 of z1, so we get a false there as well.
Now element 3 of Z1 is greater than 6.
Its value happens to be 7, so therefore, the corresponding element
in the Boolean array is true.
And in fact, all subsequent elements are also greater than 6,
so therefore all subsequent elements in the Boolean array are also true.
We can use the Boolean array, also called a logical array, to index
another vector.
But what are the elements that are returned in that case?
As you may have guessed, Python returns those elements
of the array for which the corresponding value in the Boolean vector is true.
Let's look at an example.
Let's first use the logical index vector to access elements of z1.
I'm interested in accessing elements of z1, I therefore start with z1.
I need my square brackets as usual.
Inside the square brackets, I need to put in my logical index vector, which
is, in this case, z1 greater than 6.
In this case, Python returns to me those elements
of the z1 array that happened to be greater than 6 in value.
But I can also do the same to my array z2.
Now let's think about this, what's happening here.
My index vector is still identifying those elements of z1
that happened to be greater than six.
Now in this case, I am however, using that index vector
to access elements in my array z2.
I can run this and I get an output.
I could also define my logical vector in a slightly different way.
I could explicitly construct a logical vector.
In this case, I've typed ind equals z1 greater than 6.
If we inspect the content of ind, we'll see that it's a logical vector.
I can now type z1, square bracket, ind, and I get the same output as before.
Similarly, I can type z2, ind, and the output is the same.
One final word about indexing NumPy arrays-- and this
is really important because it can easily
lead to subtle programming errors.
When you slice an array using the colon operator, you get a view of the object.
This means that if you modify it, the original array will also be modified.
This is in contrast with what happens when you index an array, in which case
what is returned to you is a copy of the original data.
Let's clarify this distinction with examples.
I'm going to define my z2 as before.
Then, I will define a new vector "w" in this case.
I'm just going to slice that, let's say, from 0 to 3.
I can look at the contents of my w.
In this case, I choose to modify the element at location zero.
So I'm just going to type w square brackets 0, is equal to 3.
I can now inspect the content of w, and instead of having 1, 3, and 5,
I have 3, 3, and 5, as we would have expected.
However, if I now type z1, you will see that the first element at location
is 0 of that array has also been modified.
Let's see what happens if we use indexing and not
slicing to access an array.
As before, I'm going to define my z1 vector.
Then I need to define my index vector, which I'm going to call 0, 1, and 2.
In this case, I've defined this as a list,
but if I wanted to define that as an array,
I simply place NumPy.array outside of my list.
Now I have two elements defined.
I have my z1 and I have my index.
I can now do the following-- I'm going to create w
by taking my object z1 and indexing that using my index vector.
The contents of w here are 1, 3, and 5.
I can now look at the element 0 of w and I can set that to be equal to 3.
If I now look at w, I I'll see that the element, the first element,
located at position 0 has been modified to 3.
If I now go back to my array z1, I see that the first element, number 1,
has not been modified.
In summary, for all cases of indexed arrays, what is returned
is a copy of the original data, not a view as one gets for slices.


'''

import numpy as np
z1=np.array([2,3,5,9,3,5,8,7,2,6])
print(z1)
z2=z1+1

print(z2)
ind=[0,1,2]
print(z2[ind])


z3=np.array(ind)
print(z3)

print(z1>6)

print(z1[z1>5])

print(z2[z1>5])

#copying by Indexing is better than slicing
#caz slicing points at the same object
#indexing
z3=z1[ind]
print(z3)
z3[0]=0
print(z3)
print(z1)