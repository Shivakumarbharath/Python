'''

Start of transcript. Skip to the end.
Our final task in the short case study is
to compare your translation to the official one obtained from the NCBI
website.
Let's look at how we read in the DNA sequence file before.
In our code, we defined first the name of the input file as dna.txt.
We then opened that file, and then we have read in the entire file in one go.
There is another way to read in an entire file, which is usually
preferred to our previous approach.
This new way involves a with statement, and the reason it's preferred
is because it's better able to cope with situations
where something goes wrong with the reading of the file.
You can read more about it online.
Here, I will just demonstrate how it works.
Let's take our existing code.
We'll just copy and paste it here above.
The first line doesn't change.
Our input file is still dna.txt.
With the with statement, the word with becomes the first statement
on the line.
The second one is open, which actually opens our file.
At the end of the line, we add as f.
In this case, we are using the with statement
to open a file we are still calling our file object, f.
We now need to indent the third line, seq equals f.read.
This is because with is a compound statement, so it ends with a colon,
and that's why the following line has to be indented.
Let's turn our sequence reading code into a function that reads in the file
and automatically replaces backslash n and backslash r
characters with an empty space.
We're going to be defining a function called read sequence, read_seq.
First, we have def.
The input argument is going to be inputfile, and we need our colon here.
The first two lines will be just reading in the file,
but I need to make sure to indent these two lines.
The next step will be to do the replacements of backslash n
and backslash r with empty space.
Again, we need to indent these.
And finally, we need to return the sequence
to whoever called our function.
So we'll say return sequence.
While the function is still fresh in our minds,
let's make sure to add a short docstring.
In this case, the function reads and returns
the input sequence with special characters removed.
Now that we have defined the function, let's
first run the definition of the function.
And we can now try using it.
I would first like to read in the protein sequence,
so we'll say prt equals read_seq.
The input is a string, protein.txt.
And the function runs.
We can also read in the DNA sequence by saying DNA
equals-- the sequence is called DNA.
And now we've read also our DNA sequence.
We can try translating the DNA sequence, but in this case,
the output is an empty string .
This suggests that there might be a problem with the length of our DNA
sequence.
If you look at the length of our DNA sequence,
we can ask if that is divisible by 3.
In this case, we have a remainder of 2, so we know that it's not.
To understand what's going on, let's go back to the NCBI website.
If you look at the website where it says CDS,
you will see two numbers next to it, 21 and 938.
These are the locations of the gene where
the coding sequence starts and ends.
So instead of taking the entire DNA sequence,
we would really like to be doing the translation starting at position 21
and ending at 938.
We can use string slicing to obtain the part of the sequence that we want.
However, we need to be careful with the indices.
If you investigate the NCBI website, you will
see that the sequence positions are numbered from 1 to 1157.
In Python, indexing starts at 0, so genome positions 21 and 938
correspond to Python string positions 20 and 937.
So the starting point of the string slice will be 20,
but the stopping location of the string is 938.
This is because when we specify the stopping location as 938,
the last character to be included is at position 937, which
is exactly what we want.
Let's try rerunning our translate function.
We take the DNA sequence-- not all of it.
In this case, we start at 20 and we want to end at 938.
In this case, we're at least getting a translation.
We can then print out our protein sequence, which is prt.
If you compare these two sequences, you will
see that they look almost identical.
The only difference between these two sequences
is the underscore character that appears at the end of our translated sequence.
So here's what's going on.
At the very end of a protein coding sequence,
nature places what's called a stop codon.
There are three stop codons, and their function
is to tell someone reading the sequence that this
is where you should stop reading.
It's almost like an end of paragraph sign.
The stop codon is not included in the downloaded protein,
because it's usually not of interest.
But when we download the DNA sequence and translate it ourselves,
the stop codon is included in the translation.
Therefore, we should really skip the last codon from our translation,
and we can modify the stopping point of the slice.
So let's try rerunning our protein translation,
but instead of ending the slice at 938, we'll end it at 935.
In this case, the protein looks identical to our downloaded protein.
To check if it is, we can ask Python if prt, the downloaded protein,
is equal to the translated protein.
When we run this line on the screen, Python
returns true, which means success.
An alternative approach is the following:
The function translate returns a string of amino acids.
So instead of omitting the last three characters from the DNA sequence,
I can just omit the very last character of the translated amino acid sequence.
Let's try running that.
In this case, we want to translate the protein all the way to location 938,
but we want to exclude the last character of the translation.
That's why we slice the output from the very beginning,
and we only exclude the last character.
Again, our translated protein and the protein sequence we have downloaded
are identical.
We have accomplished four tasks in this case study.
First, we have manually downloaded the DNA and protein sequence data
from the website.
Second, we imported the DNA data into Python.
We then created an algorithm that translated the DNA using a dictionary.
Finally, we checked that the DNA translation
matched the downloaded amino acid sequence, the protein
string, which it did.
I hope you both enjoyed this case study and learned a lot of Python.



'''


def read_file(input_file):
    with open(input_file,"r") as f:
        seq=f.read()
    seq=seq.replace('\n','')#so that they are in one line
    seq = seq.replace('\r', '')
    return seq

def tranlate(seq):
    """
    THIS FUNCTION TRASNSLATES DNA STRANDS TO PROTIENS


    :param seq:
    :return: PROTIEN
    """
    table={
    'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
    'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
    'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
    'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
    'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
    'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
    'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
    'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
    'GTA':'V','GTG':'V','GTC':'V','GTT':'V',
    'GCA':'A','GCG':'A','GCC':'A','GCT':'A',
    'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
    'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
    'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
    'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
    'TAC':'Y','TAT':'Y','TAA':'_','TAG':'_',
    'TGC':'C','TGT':'C','TGA':'_','TGG':'W',
    }
    #check lenth of the sequence is divisible by 3
        #loop over the sequencep
            #extract the single codon
            #Look up the codonand store the result.
    protien=''
    if len(seq)%3==0:
        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            protien+=table[codon]

    return protien

dna=read_file("dna.txt")
down_pro=read_file('Protien.txt')
pro=tranlate(dna[20:938])[:-1]
#or
#pro=tranlate(dna[20:935])

print(pro)

if pro==down_pro:
    print("Successfull")
