'''

art of transcript. Skip to the end.
The best way to read a file depends on what you'd like to do with the file.
If you need to read a large file, but you're only
interested in some of the lines, not all of them,
you could read the file in a for loop, one line at a time, process the line,
or skip it, and move onto the next line.
We've seen an example of this earlier in the course.
This approach leads to memory efficient and fast code.
Another option is to read the entire file in one go.
In this case, we will be doing that because we do not need
to skip over any lines in the file.
Before you start working with files, make sure
that your Python working directory corresponds to the directory
where you downloaded your files.
You can type pwd, which stands for print working directory, in your IPython
shell.
And, in this case, I do need to move to a different directory.
CD stands for change directory.
I'm going to go to Python case studies.
Then I'll issue cd again.
I want to go to the translation case study.
I can now say pwd again, and my working directory has now been changed.
Now, let's read the file.
Let me first specify the name of the input file.
I'm going to call that variable input file.
And, in this case, it's dna.txt.
I'll then be using the open function to open the input file.
The second argument is r which is short for reading.
I want to capture the file object here.
I'm going to call that f.
And, finally, I can use the f.read method to read the entire file.
I want to make sure that I capture the contents of that file.
In this case, what I am reading is a sequence,
so I'm going to call that variable seq.
So seq = f.read.
I want to move this code here in my editor for later use.
And now we can look at the sequence.
You can either say print seq or you can just type seq.
So it looks like the reading operation was successful.
If you look carefully, you can see some additional characters in the text.
It looks like backslash n appears in the text with some frequency.
This is a special character that affects the way the string gets printed,
and we ended up with these extra characters
because we copy pasted the text from a web browser to the editor.
You can see how these characters affect the way the string is printed
by asking Python to print the data.
So we type print seq,
and you see that the data appear differently on the screen.
These extra characters will cause problems for translation
so how could we remove them?
An easy way is to use the replace method which takes two arguments--
it replaces every occurrence of the first argument substring
with the second argument, another substring.
We can type seq.replace.
The first is going to be "\n",
that's what gets replaced,
and we will replace that with nothing.
Because strings are immutable, the method returns a new string.
So in order for us to use the new string,
we need to assign it to a variable.
In this case, I'm going to reassign it to the same variable as before.
We'll take the same comment we had before.
I'll just type seq = seq.replace.
Let's try printing seq.
And, in this case, we do not have those extra line breaks
that we had there before.
Let me take this line of code and move it up to the editor for future use.
Sometimes there may be another character hiding in a string,
and depending on your computer, it may or may not be visible.
Just to be on the safe side, let's remove that as well.
There is no harm in running this extra step
because if you don't have the extra character nothing happens.
We'll be using the same command as before.
But, in this case, we will be removing the backslash r character
and we'll replace that with nothing.
I will again take and copy paste this line here,
and we are ready to move on.



'''

input_file="dna.txt"
f=open(input_file,"r")
seq=f.read()
#seq=seq.replace('\n','')#so that they are in one line
seq=seq.replace('\r','')#there will be an extra invisible charecter

print(seq)