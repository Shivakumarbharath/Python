'''

ranscript. Skip to the end.
Before we start coding the function itself
it's helpful to create a test string.
I'm going to call that text, and I'll just
copy paste a short string that I wrote previously.
The purpose behind having a text string like this
is to be able to test our function as we make progress with it.
Since this function will keep track of all unique words
and count their frequencies, I'm going to call this function count_words.
It's a function so we'll need the def statement
and the input argument is going to be just simply text in this case.
We agreed that using a dictionary would be
a good solution for this specific task.
I'm going to create an empty dictionary called word_counts.
The next step for us is to break the text down into words.
To accomplish that we'll be using the split method and the character
we want to use for splitting is just an empty space.
This will give us a list that we can loop over so this calls for a for loop.
Because the items in the sequence or list are words,
I'm going to be using word as my lop variable.
So for word in text.split.
And now we're ready to loop.
There are two possible things that can happen as we loop over our text.
We can either come across a word that we've seen before, in which case,
we have to increase the counter associated with that word by one.
In case we see a word we haven't seen before,
we have to establish that entry in the dictionary
and initialize the counter to be equal to 1.
So let's divide this into two subtasks.
We have the case where we have a non-word
and the second case is where we have an unknown word.
Let's deal with the non-word case first.
What we'd like to test for is, whether this word
has appeared in this dictionary before.
This calls for an if statement.
If word in word_counts.
So now we know that we have seen this word before.
What we need to do is we need to access our dictionary word_counts
and we want to increase the counter that's
associated with this specific word.
We want to increase that by 1.
And I'm using the shorthand operation here.
This is the non-word case.
The other situation is where we come across a previously unseen word.
We can use the else statement here.
In this case we still like to access the word_counts dictionary.
But in this case we have to set that counter to be equal to 1,
because this is the first instance of the word that we're seeing.
That deals with the second case, the unknown word.
At this point, we are ready to return the dictionary
to whoever called the function.
We need one more statement in our code, in our function,
which is the return statement.
So we need to return word_counts.
Before we move on, let's make sure to add a docstring in our function.
Now that we have defined the function, let's run it.
And the function has now been defined.
We also want to make sure we have our test text defined
and now we can try running the function and see what happens.
And as expected Python returns a dictionary to us
where the keys are words, unique words,
and the values associated with these keys
are the number of times each word occurs in the text.
Having some test data handy is very useful.
Looking at the dictionary, one obvious shortcoming of our current routine
is that it includes punctuation like periods, or full stops,
as part of the word.
This would lead to an inflation of the word count
because, for example, a word that appears in the middle of the sentence
will be counted separately from the same word
if it appears at the end of a sentence and is immediately
followed by a period.
Another problem is that if the word appears at the beginning of a sentence,
its first letter is capitalized, again giving rise
to double counting of some words.
To address these issues, we're first going to turn the text into lower case.
This means that any word, whether capitalized or not,
will count as one word.
Addressing punctuation is a bit more complex.
Our strategy is to first specify all the punctuation marks
that we'd like to skip, and then loop over that container
and replace every occurrence of a punctuation mark with an empty string.
As the first task we need to turn the text into a lower case.
We can do that using the lower method and then
we just have to recapture that new text.
So we're typing text=text.lower.
The second thing we need to do is, we need
to define the characters that we will be skipping
as we're looping over the text.
We'll construct a list for this purpose, and we
can include a few of the most common punctuation marks
here that we'd like to skip.
For example we can include period, comma, semi-colon,
colon, have single quote, and we can also include double quote.
In this case we have to use single quotes for Python's own string.
The reason we cannot use double quotes for the last string is because double
quotes are also used to begin and end a string.
This is why we'll be using single quotes, which
surround the character that we really want to represent,
which is a double quote.
The next step for us, is loop over all of the skip characters
and replace them with an empty string.
This calls for a for loop.
We'll be taking our text and we will replace ch, the skip character
in question, with an empty string.
We then also want to capture the modified string that the replace method
returns, and this part is done.
Finally, to complete this modification to our function,
we want to make sure to update the docstring
to reflect the change we just made.
We'll just say skip punctuation.
Let's then run the definition of our function.
And now we can try running the function using our test
string that we had defined before.
In this case, looking at the output, it's a dictionary before,
but you'll notice said all of the keys are lowercase, which is what we wanted.
We also go to def the punctuation marks that we included in the skips list.
It's useful to be able to write your own counting routine like we just did.
However, counting the frequency of objects
is such a common operation that Python provides
what is known as a counter tool to support rabbit tallies.
We first need to import it from the collections module, which
provides many additional high performance data types.
The object returned by counter behaves much like a dictionary,
although strictly speaking it's a subclass of the Python dictionary
object.
Let's modify our function to use the counter object.
In this case, I would like to retain both my original function and the one
that uses to counter object.
Our first step is going to be to import that,
so from collections import counter.
To start the function I'm going to take my previous function
and I'm just going to copy paste it here underneath.
This is the code that I'll be working with.
Because this is a different function because it's
using the counter object from collections,
I'm to call this something else.
I'm going to add the word fast at the end.
The counting takes place in the last few lines of the code.
We don't change the first part where we simply convert the text to lowercase,
and we also want to keep the part that skips over punctuation characters.
The only thing that will be changed is the looping
over individual words in our text string.
The last several lines of the code can all simply
be replaced with a single expression.
We will define word_counts on this line, which is the first time we're using it.
The input to our counter object will be the text
that we would like to use for counting.
We'll take our text, we'll split it to get the words, and we're done.
Before we run the function let's first do the import.
We can now run the definition of the function
and then we can test it on our test dataset.
In this case, again as expected, the function
returns a counter object which looks essentially identical to the dictionary
object.
Let's see if the objects returned by these two different functions
are actually the same.
We'll first call the count_words function using our text.
And we want to ask Python if that's equal to the object which is returned
by count_words_fast on that same input.
In this case, the answer is true, therefore
we know that these two different implementations of the same function
return identical objects.


'''

text = "This is my test text. Help me finding the mistake in my text, now this is my text"


def count_words(text):
    """



    :param text:
    :return a dictionary of number of words :
    """
    count = {}
    text = text.lower()
    skips = [".", ",", ":", ";", '"']
    for skip in skips:
        text = text.replace(skip, '')

    for word in text.split(" "):
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


print(count_words(text))

# using the inbuilt function
from collections import Counter


def count_words_fast(text):
    """

    to count the number of times a word is repeating

    :param text:
    :return a dictionary of number of words :
    """

    text = text.lower()
    skips = [".", ",", ":", ";", '"']
    for skip in skips:
        text = text.replace(skip, '')

    count = Counter(text.split(' '))
    return count


print(dict(count_words_fast(text)))
