'''

Start of transcript. Skip to the end.
Let's talk about scope rules next.
Consider a situation where, in different places of your code,
you have to find several functions called "update,"
or several variables called "x."
How do we know which update function or which x variable
Python uses at any given time?
We know from before that each variable name belongs
to a certain abstract environment or namespace,
and we can think of it as a context in which a given name exists.
This is analogous to many everyday situations that require
a context for names to be meaningful.
So when you talk about your friend John, your other friends
know intuitively which John you're talking about.
But how does Python know which update function to call
or which variable x to use?
The answer is that it uses so-called "scope rules"
to make this determination.
It searches for the object, layer by layer,
moving from inner layers towards outer layers,
and it uses the first update function or the first x variable that it finds.
You can memorize this scope rule by the acronym LEGB.
It may not be the catchiest acronym, but it works.
Here's what the different letters stand for.
L stands for "local," E stands for "enclosing function," G for "global,"
and B stands for "built-in."
In other words, local is the current function you're in.
Enclosing function is the function that called the current function, if any.
Global refers to the module in which the function was defined.
And built-in refers to Python's built-in namespace.
If Python cannot resolve the name, meaning if it cannot find an object
having the name you've requested, it raises a so-called "name error
exception."
And the execution of your program typically stops at this point.
Let's practice scope rules first by defining
a function called "update" that has no parameters-- def update parentheses
and colon.
Then we have x dot append 1.
All this function does is that it appends, or at least tries to append,
the number 1 to an object called x.
When we run this function update, Python gives us a name error
and tells us that a name x is not defined.
Let's see what happens if we define a list called "x,"
and then call the function.
x is a list consisting of two elements, 1 and 1.
And then we call the function "update."
You might be surprised to see that the code now
runs and appears to modify the list x.
To understand what is happening, let's go through the steps
that Python goes through when it tries to find object x.
Using the LEGB rule, it first looks for x in the local scope,
inside the function update.
But x does not exist within this scope.
It then moves on to the next layer, which is enclosing functions.
But in this case, there are no enclosing functions,
because we didn't call the update function from inside another function.
So let's move on to the next layer, which
is the global layer, the module or namespace where the function update was
defined.
The global layer or scope does contain an object called x.
It is the x that we defined right here.
And since it is the first object of that name that Python found,
this is the object that it will use.
This example focusing in scope rules shows
that you can manipulate global variables,
variables defined in the global scope, from within functions.
Functions that modify either their inputs or objects defined
in other parts of the program in this type of behind the scenes manner
are said to have "side effects."
For example, if you look at the function call, which in this case
is simply update followed by parentheses,
it is not clear that the function has side effects.
This is a programming style that you should generally avoid,
because it can lead to programming errors that are very difficult to find.
Let's then consider a slightly more complex example about scope rules.
This example demonstrates both scope rules and mutability and immutability
of Python objects.
To get going, let's first write two short functions.
Our first function is called "update."
And our second function is called "main."
In this case, the main function calls the update function
as part of the program.
We would like to know what are the values of n
and x at different points of the program's execution.
Let's try to figure it out first without running the code,
and we can then check our answer against a program's output.
Let's first get a sense of the program's overall flow.
We first call main.
Main calls update.
The execution then returns to main.
And once main exits, we return the global scope,
the scope where we defined the functions main and update.
Let's first look at the code in main.
Here, n and x are assigned in the function main,
so when we get to the first print function,
Python finds the objects n and x in the local scope,
meaning that the values of the objects are n equal to 1
and x is equal to 0, 1, 2, 3, a list.
The program then calls the function update with arguments and n and x.
So the program's control then moves to the function update.
All of the function update has a parameter, n.
On the first line of the function, we have an assignment,
n equals 2, which creates a new variable that happens to be called "n,"
And its value is set to 2.
On the second line, we append the number 4
to the object x, which is one of the function's parameters.
Just to be clear on terminology, remember
that an argument is an object that is passed to a function as its input
when the function is called.
A parameter, in contrast, is a variable that is used in the function definition
to refer to that argument.
That means that the second line will append the number 4 to the list
that we have created in the main function.
So when we get to the print function, Python
finds the objects n and x in the local scope,
meaning that the values of the objects are n equal to 2
and x is a list, 0, 1, 2, 3, 4.
Python then exits the function and control returns to the main function.
Remember that variables that are created within a function, such as n
in the case of the update function, are deleted
as soon as Python exits that function.
Looking at the final print function, the objects n and x
are found in the local scope where n is equal to 1
and x is a list, 0, 1, 2, 3 4.
We can check our reasoning by running the program.
If this example or some of the steps that we have just gone through
are unclear to you, go through the example
again, at each point using the LEGB rule to figure out how Python
determines which n and x object to use.

'''


def update(n, x):
    n = 2
    x.append(5)

    print('Update', n, x)


def main():
    n = 1
    x = [0, 1, 2, 3, 4]
    print('main', n, x)
    update(n, x)
    print('main', n, x)


main()
