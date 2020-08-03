'''

art of transcript. Skip to the end.
The translation process is essentially a table lookup operation.
Python provides a very natural object for dealing
with these types of situations.
This object is a dictionary.
In this case, the key objects are strings,
each consisting of three letters drawn from the four letter alphabet.
The value object is also a string but a string
consisting of just one character.
Defining a dictionary can be somewhat tedious.
In this case, we've already done this work for you.
We've created a dictionary called table where
the keys are strings corresponding to codons or nucleotide triples.
And their values are also strings which correspond to common one-letter symbols
used for the different amino acids.
Let's then open the file table.py.
It's in my python_case_studies translation dictionary.
I'm going to open that.
And I'll just mark the table, making sure to get the full table.
I will then go back to my editor here, and I'll
copy paste the dictionary in here.
You'll see that the table dictionary appears indented.
This is going to cause problems.
So I want to make sure I will de-indent the dictionary.
And now we're good to continue.
Let's first make sure we know how to use this translation table.
How would you look up the key that corresponds to CAA or CCT or GTA?
I'm going to first just type table.
And I might initially type CAA.
But this is a problem because the keys themselves are strings.
That's why I need to provide a string as an input.
And now I get the desired output.
To look up CCT I can just change to string CCT,
and the output is P. Let's then think about how to approach this problem.
Here are the steps that I would take.
First, I would check that the length of the sequence is
actually divisible by three.
It should be, but sometimes things go wrong so it's important to check this.
Next, I would look up each three-letter string in our table
and store the result somewhere.
Finally, you keep doing this in a loop until you
get to the end of the sequence.
Let's write some informal pseudocode step-by-step instructions
on how to proceed.
Let me first create some space here in my editor.
The first task I would like to do is to check the length of the sequence.
So, you might say something like check that the sequence
length is divisible by three.
If that's true I can then loop over the sequence.
For each iteration of the loop I will need to extract a single codon.
And finally, I need to look up the codon and store the result. Look up the codon
and store the result.
This is certainly not a formal pseudocode
but these step-by-step instructions will hopefully help us
as we start writing the actual code.
Here we're going to check the length of the sequence.
For a number to be divisible by three it must be that division by three
yields a remainder of zero.
Python, like many other languages, has a so-called modulo operator that
yields to remainder from a division.
If you haven't come across the modulo operator
this would be a good time to go online and search for it.
Let's look at a couple of examples of the modulo operator.
7 divided by 3 yields 2.33.
Let's do 6 divided by 3.
That gives 2.0.
In the first example, we would expect to have remainder, but in the second
we would not.
So we go back to the example 7 divided by 3
and we replace division with modulo.
The result is 1.
3 divides 7 twice and 1 is left over.
Let's look at the second example, 6 divided by 3.
If we do 6 modulo 3, in this case, 3 divides 6 exactly twice
and nothing is left over.
Let's look at the length of the sequence.
And we can then ask if this is divisible by three?
In this case, the answer is no.
And this is something that we'll come back to later.
Lets start writing the code here.
So we are now dealing with the first step in our pseudocode.
We'd like to ask if the length of sequence modulo 3 is equal to 0.
If that's the case, then we do have a valid sequence
and we can proceed with the code.
If you try running this, we can remove the first comment here,
if you try running this you'll see that it will not run.
That's because if it is a compound statement
and Python expects something to be on the following line.
We can use the pass statement here if we'd like to run the code.
It doesn't do anything, which may sound odd,
but it's helpful when Python syntax requires
some statement, as is the case here.
We can now try rerunning this, and the code runs.
Let's then think about the loop.
To loop over the sequence one character at a time
we could use the following structure.
We can type for s in seq.
And then we might just print s.
We could build our codons one character at a time but in this case,
string slicing is probably a better alternative.
Let's take our sequence and let's slice it.
The starting point of the slice is 0 and the end point is 3.
Remember, in this case, when you're slicing
a string the elements that will be located
are those at positions zero, one, and two.
In other words, Python stops before it hits the stop index.
If I'd like to look at the next element, I want to start at 3 and end at 6.
To look at the third element of the sequence I would start at 6
and end at 9, and so on.
So to start a slice I need to sequence 0, 3, 6,
and so on for the starting locations.
The endpoint is always going to be the starting point plus three.
This seems to call for a range object.
For a range object we specify the starting point first, say
0, the end point, let's say 11, and the step size.
In this case, we've defined a range object.
But if we want to print out the values we need to first turn that into a list.
So I'm constructing a range object but to see the actual values in the range
object I will turn that into a list.
We can now continue with our code.
I then want to take my range object and move it to my code here.
This replaces the pass statement.
This is going to be a for loop.
So we'll say for i in range starting from zero we
want to go to the end of the sequence.
So the length of the sequence goes in here.
And we go in steps of three.
This is the looping over the sequence part.
So this line is now done.
The next step is going to be extracting a single codon.
I'm going to call that codon because that makes sense.
I'll take my sequence, and the first starting point is going to be i.
And I will slice from i to i plus 3.
Again, this enables me to extract the codon.
I can try running this code.
And we see that the code runs.
The next step is to look up the codon and store it.
We can store the protein in a string and concatenate amino acids to it
one at a time.
Let's go back to our code.
I will first initially need to create my protein.
I'm just going to call the protein.
And it's going to be an empty string.
Once I've extracted my codon I need to look it up.
Remember, my table is called table, that's my translation table.
I can look up my codon by typing table codon.
And this is my new amino acid that has to be appended to the end of protein.
Protein is a string so we can concatenate the existing protein
string to the new string, which is created
by the table codon expression here using the shorthand notation plus equals.
So in this case, we're looking up each codon one at a time
and we are concatenating that to the existing protein string.
I've now completed the last line.
So I'm going to erase that and I'm going to try running my code.
The code runs so at least we know that we don't have any syntax errors so far.
It's helpful to turn our code into a function
so that we can easily call it using different sequences.
First I need to start with the def statement.
I'm going to call this function translate
because it translates the input sequence, a DNA sequence,
into a sequence of amino acids.
We need a colon on at the end of the function definition.
We then need to indent the code that I have here.
Finally, we need a return statement that returns the protein
to whoever called this function.
And our function should be ready at this point.
Let's then try running the definition of the function.
And in this case, we are not getting any error messages,
which is what we wanted.
We can also try actually running the function.
We've now defined it but we haven't actually run it yet on any input data.
Let's look at a couple of simple examples.
I'd like to translate say, ATA, and the result should be I, which is correct.
Let me try one more example.
I might want to translate triple A, and the answer should be K.
So, so far we're in good shape.
While we're at it, let's add a docstring to our function.
A docstring is a string literal that occurs
as the first statement in a module function,
or a class, or a method definition, and it becomes part of that object.
You or somebody else can then use the help function
to learn more about the function using the docstring.
The docstring should summarize the behavior of the function
and document its arguments, returned values, possible side effects,
and anything else that would be important for a user
to know about the function.
While the function is still fresh in our minds,
let's try writing a short docstring.
Here's an example of a docstring that I wrote earlier.
Make sure to include your docstring inside the function definition.
We can now rerun the definition of the function which contains the docstring.
We have just redefined it.
If I now type help translate you'll see that the docstring
has become part of the function.


'''
input_file = "dna.txt"
f = open(input_file, "r")
seq = f.read()
# seq=seq.replace('\n','')#so that they are in one line
seq = seq.replace('\r', '')  # there will be an extra invisible charecter


def tranlate(seq):
    """
    THIS FUNCTION TRASNSLATES DNA STRANDS TO PROTIENS


    :param seq:
    :return: PROTIEN
    """
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTG': 'V', 'GTC': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCG': 'A', 'GCC': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    # check lenth of the sequence is divisible by 3
    # loop over the sequencep
    # extract the single codon
    # Look up the codonand store the result.
    protien = ''
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protien += table[codon]

    return protien
