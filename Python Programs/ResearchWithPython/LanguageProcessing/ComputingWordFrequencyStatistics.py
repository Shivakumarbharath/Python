'''

f transcript. Skip to the end.
Given a dictionary or a counter object from the collections module,
we would like to know how many unique words there are in a given book.
We'd also like to return the frequencies of each word, meaning,
count-specifying how many times each word has appeared.
To do this we'll be writing a word stats function.
Our function is going to be called words stats, short for word statistics.
And the input is going to be word counts, which
is returned to us by the other function we previously wrote.
The first thing we want to accomplish is to count the number of unique words.
To do that we can take the word counts object
and simply ask what is the length of that object.
We know that each entry in the dictionary is going to be unique
and therefore the length of that object is
going to return to us the number of unique keys we have,
meaning the number of unique words.
I'm going to call this number unique, num unique for short.
And this accomplishes the first part.
The second task is to return the word counts for every single unique word
in the dictionary.
We'll start with the word counts dictionary.
We'd like to extract the values the counter is from this object, which
we do using the values method.
I'm going to simply call this counts and that's the frequencies
of each word in our text.
Finally, we need to return these two objects.
So I'll be returning a tuple, which consists of num_unique and counts.
Let's add a short docstring.
We can do just a simple one-line docstring here
saying return number of unique words and word frequencies.
Let's then try running our function.
Let's first read in the text, the book.
Here is the path to Romeo and Juliet.
So we're just trading the text.
Then let's count the words.
So word counts is equal to count words in text.
And then we can ask the word stats to return
the number of unique words and the word frequencies to us.
If we look at the contents of number unique
we know that Romeo and Juliet has a total of 5118 unique words.
If we'd like to know how many words there are in total
we can do a sum of the counts,
and it's approximately 41,000.
Let's use the word stats function to compare Shakespeare's Romeo and Juliet
in English with its German translation.
I will first take the code that we have here
and I will copy paste that in the editor above.
So we first read the text.
We then perform the word counts.
And then we run our word stats function on what we just read.
All of these operations will be identical for the German version,
except for the name of the book.
We first have to go to our German directory,
and in German it's called Romeo und Julia.
Then we'd set print function here.
Number unique and some counts.
That takes care of that.
We'll use the same exact line here.
We'll create a little space here.
Let's try running this.
We know the result for English.
Same as before, which is good.
We'll do the same operation for the German version
and we'll find the outcome is a little different.
The German translation of Romeo and Juliet
appears to contain about 7,500 words, but in length it's about 20,000.


'''

def word_stats(word_counts):
    """
    Returns number of uniqe words and frequency of repetation
    :param word_counts:
    :return:
    """
    num_uniqe=len(word_counts)
    freq=word_counts.values()
    return (num_uniqe,list(freq))


