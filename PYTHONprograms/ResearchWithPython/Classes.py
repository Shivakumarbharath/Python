'''

art of transcript. Skip to the end.
Our emphasis has been and will be on functions and functional programming,
but it's also helpful to know at least something about classes
and object-oriented programming.
In general, an object consists of both internal data and methods
that perform operations on the data.
We have actually been using objects and methods all along,
such as when working with building types like lists and dictionaries.
You may find at some point that an existing object type doesn't fully
suit your needs, in which case you can create
a new type of object known as a class.
Often it is the case that even if you need to create a new object type,
it is likely that this new object type resembles,
in some way, an existing one.
This brings us to inheritance, which is a fundamental aspect
of object-oriented programming.
Inheritance means that you can define a new object
type, a new class, that inherits properties from an existing object
type.
For example, you could define a class that does everything
that Python's built-in lists do, and then add an additional method
or methods based on your needs.
As a quick reminder of how we've been using methods so far,
let's define a list, ml, which consists of a sequence of numbers.
If I wanted to sort this list, I can use the sort method which
is provided by the ml object, a list.
If I now look at the contents of the list,
we can see that the values have been sorted.
Let's look at an example of how to create a new class,
essentially a new type of Python object.
A class is defined using the class statement.
Class, MyList, and colon.
The name of the class-- in this case, MyList-- immediately
follows the word, "class".
Notice that we placed parentheses after MyList.
This is how Python specifies inheritance.
When a class is created via inheritance, the new class
inherits the attributes defined by its base class, the class it is inheriting
attributes from-- in this case, a list.
The so-called derived class, in this case "MyList",
can then both redefine any of the inherited attributes, and in addition
it can also add its own new attributes.
You can think of the class statement as setting up
a kind of blueprint of a new class.
What that means is that it specifies the internal structure of these new types
of objects, including what methods and operations
they support, but it does not create any object of that type.
When an object of a particular type is created,
that object is sometimes called an "Instance" of that type.
So another way to state what I just said is that the class statement doesn't
create any instances of the class.
This is a bit like defining a function with the def statement --
the function definition specifies what the function does when called
but defining a function does not, in itself, call or invoke that function.
That's something you would do outside of the function's definition.
That's why it's helpful to think of the class statement
as defining a blueprint of the new class, a new type of Python object.
Our class makes use of the min and max functions, as well as the list
remove method, so let's review those briefly.
Here we have a list set up called x.
I can use the min function to find the smallest element of the list, x--
in this case, the number two.
Similarly, I can use the max function to find the maximum element of the list--
here, 11.
Let's also remind ourselves how to remove elements from a list.
The method "remove" does precisely that, and it
takes just one argument, which is the value that you'd
like to remove from the list.
One thing to note is that if the given value appears on the list
multiple times, only its first occurrence is removed.
Continuing with our list x-- one of the elements in the list is number 10.
So if we type, x.remove(10), and we look at the list again,
we can see that the number 10 has been removed from the list.
Let's look at the class definition that I've just completed on my screen a bit
more closely.
You can see that it contains two def statements
that I used to define functions.
The functions defined inside a class are known as "instance methods"
because they operate on an instance of the class.
By convention, the name of the class instance is called "self",
and it is always passed as the first argument
to the functions defined as part of a class.
Here we define two functions, two instance methods,
which we call remove_min and remove_max.
Looking at the remove_min function, we see that it only consists of one line.
We first use the min function to find the smallest element of the list.
We then use the remove method to remove that element from the list.
The function "remove_max" works analogously,
except that instead of the min function, we
have the max function inside the parentheses.
Let's then demonstrate the use of our newly defined class, MyList.
I'm going to define the Python list, x, consisting of a bunch of numbers.
I'm then going to define an object, y, which is in MyList,
and it contains a copy of all of the numbers in x.
Remember, we can use the dir function to ask what methods
are available for any given object.
In this case x is a standard Python list
so it supports all of the methods of Python lists.
We can then do the same for our object, y, which remember
is the class we wrote ourselves.
Here, if you look at the last couple of lines,
you'll see that the method to remove max and remove min are now available.
We can use these methods, so let's type y.remove_min,
and if we then look at the contents of y, we'll see that the number one,
which was the smallest element, has disappeared.
It has been removed.
If we then use the remove_max method, and we again look at the content of y,
we'll see that the largest element, number 10,
has been removed from MyList.


'''


