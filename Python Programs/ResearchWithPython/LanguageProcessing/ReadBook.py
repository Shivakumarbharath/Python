'''

rt of transcript. Skip to the end.
We're familiar by now with reading files.
But here we'll include an additional argument.
Character encoding refers to the process how
computer encodes certain characters.
In this case, we'll use what is called UTF-8 encoding, which
is the dominant character encoding for the web.
We will also replace backslash n and backslash r characters.
Since this function reads a book we're going to call it simply read_book.
The input argument requires the path of the title of the book
so we'll call this argument title_path.
Since we're defining a function we need the usual def statement
at the beginning.
We're going to start this time by writing the docstring.
This function will read a book and return it as a string.
We'll be using the with statement that we saw in the previous case study.
So with open(title_path) we're opening the file for reading.
And then we need to specify encoding, which in this case is utf8.
We will open this file as current_file.
We'll get the text by reading in the current_file.
The missing step for us is to replace the backslash n
and backslash r characters with an empty string.
So we take our text, we'll first replace backslash n with an empty string.
This returns a string
and we can just train the second replace method right after the first.
In second replace we're replacing backslash r with an empty string.
Finally, we need to make sure to capture the object that we have just created.
At this point, all that is left there to do
is to return our text object to the caller.
We can try out our code
so let's try reading in Shakespeare's Romeo and Juliet.
We'll first run the function definition so our function is defined.
At this point, we are ready to read in a book.
In this case, I'm just going to be entering the path manually.
Looking at the length we'll see that Python
has read in approximately 170,000 characters, which is
all of Shakespeare's Romeo and Juliet.
There's a famous line in Romeo and Juliet.
Let's see if we can find it.
To do this we'll be using the find method.
The line starts, "What's in a name?"
The find method will return the index if it finds the substring.
Let's see what happens.
In this case, we have an index returned by the find method
so we know that the substring is part of the text.
Let's extract a sample text starting from this location.
So we'll say, sample_text equals text.
We'll start from index.
We'll do a slice that contains 1,000 characters.
And let's look at the sample text.
In this case, we will see the sample text does start
with the famous line, "What's in a name?"
So we found the appropriate line.


'''


def read_book(file_path):
    """

    To read the book and save as a string
    :param file_path:
    :return string:
    """
    with open(file_path, 'r', encoding="utf-8") as book:
        text = book.read()
        text = text.replace('\n', '').replace('\r', '')
    return text
