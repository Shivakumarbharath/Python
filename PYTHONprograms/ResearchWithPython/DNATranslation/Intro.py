'''

Start of transcript. Skip to the end.
Life depends on the ability of cells to store, retrieve, and translate
genetic instructions.
These instructions are needed to make and maintain living organisms.
For a long time, it was not clear what molecules
were able to copy and transmit genetic information.
We now know that this information is carried by the dioxyribonucleic acid
or DNA in all living things.
DNA is a discrete code physically present
in almost every cell of an organism.
We can think of DNA as a one dimensional string of characters
with four characters to choose from.
These characters are A, C, G, and T. They
stand for the first letters with the four nucleotides used to construct DNA.
The full names of these nucleotides are adenine, cytosine, guanine,
and thymine.
Each unique three character sequence of nucleotides,
sometimes called a nucleotide triplet, corresponds to one amino acid.
The sequence of amino acids is unique for each type of protein
and all proteins are built from the same set of just 20 amino acids
for all living things.
Protein molecules dominate the behavior of the cell
serving as structural supports, chemical catalysts, molecular motors, and so on.
The so called central dogma of molecular biology
describes the flow of genetic information in a biological system.
Instructions in the DNA are first transcribed into RNA
and the RNA is then translated into proteins.
We can think of DNA, when read as sequences of three letters,
as a dictionary of life.
In this case study, we will first download a DNA strand as a text file
from a public web-based repository of DNA sequences.
We will then write code to translate the DNA sequence
to a sequence of amino acids where each amino acid is
represented by a unique letter.
We will also download the amino acid sequence to check our solution.
In the process, we will also brush up on basic Python skills.
To make the problem a bit more concrete, let's first
think about it conceptually.
The input to our program is going to be a DNA sequence that
consists of a four letter alphabet.
We then read this sequence three letters at a time,
translate each triplet to a single letter
that stands for a specific amino acid, and then proceed
to the next set of three letters.
We do this until we have reached the end of the input sequence.
Here is part of the table that we'll be using to do the translation.
The actual table is longer than this.
The input is shown on the left and the outward as shown on the right.
In general before you start writing any code,
make sure you really understand the problem.
Sometimes it's helpful to run through a simple example on a piece of paper
before even thinking about the code itself.
Let's consider the following input sequence.
How would you translate this sequence?
So first we identified the first triplet, which in this case is ATA.
That corresponds to an I. We then move on to the next triplet,
CAA, which corresponds to a Q and so on.
The third triplet, DGG, corresponds to W,
and the final triplet, CAA, corresponds to a Q again.
So a translation of this DNA sequence would be IQWQ.
Just to be clear, the top line in this example
corresponds to our DNA sequence and the bottom line corresponds
to our sequence of amino acids.
Instead of doing this manually, we want to write a Python program that does
the translation for us automatically.
In this case study, we have four tasks.
The first task is to manually download DNA and protein sequence
data to your computer.
The second task is to import the DNA data into Python.
The third task is to create an algorithm that
translates to DNA using the translation table we will provide.
The fourth task, the final task, is to check if your DNA translation matches
the protein string you have downloaded.


ATA ->I
ATG ->M
CAA ->Q
TCT ->S
TGG ->W





Our first task is to manually download the data we need in this case study.
The NCBI is the National Center for Biotechnology Information,
and it is United States' main public repository of DNA and related
information.
We will download two files from the NCBI.
The first is a strand of DNA and the second
is the corresponding protein sequence of amino acids translated from this DNA.
First, we want to enter the website of the NCBI.
You can either go there directly or you can Google N-C-B-I. In this case,
it's the first hit that comes up.
Now you'll see at the top, where it says All Databases.
We're interested in downloading a Nucleotide sequence
so we scroll down until we get Nucleotide.
And in this field we need to enter a specific code that corresponds
to the sample that we want to download.
Here you need to be careful to type in exactly the following:
capital N, capital M, underscore 207618.2.
Once you have entered this exact string you can hit Search.
If you did your search correctly you should see the same page
that we have here up on the computer.
This page contains a lot of information about this specific sample.
We are primarily interested, first, in the DNA sequence.
The DNA sequence is shown at the bottom of the page
but the best way to download these data is the following:
You can go to the very top of the page, you can click FASTA,
and then you have the sequence here on the screen.
You can then use your mouse and your cursor to highlight the sequence.
Make sure you include the very first letter, which is G,
and the very last letter, which is T. We can copy that,
and then we go to our Spyder editor.
I like to create a new file here so I just click New File.
I then delete whatever happens to be on the screen.
And the next step is to paste the DNA sequence into the editor.
The next step for us is to save this DNA sequence.
I have previously created a directory that I have called python_case_studies.
I first go there.
This case study is a translation case study
so I will be selecting that folder.
I want to call this file dna.txt, and I recommend
you use that same file name convention.
I then have to choose a dot txt in the menu
here because we're saving a text file not a Python file.
And if all goes well, you should now have dna.txt
in your python_case_studies directory.
Let's then go back from our sequence page, the main page for this sample.
And to download the amino acid sequence you can click CDS.
CDS stands for the coding sequence.
If you look at the bottom right corner of your screen,
you will see the translation here at the bottom of the pop-up window.
I'm going to select that.
Then I'll go back to my Python editor.
I'll open a New File.
I'll remove whatever is in this file, and then I will paste the amino acid
sequence into the editor.
I will then go to Save.
I will then pick my previously created python_case_studies directory.
I go to translation.
And I'm going to call this file protein.txt.
Again, it's a text file so I need to make
sure I choose text file in the menu.
And now we have downloaded both the DNA sequence and the protein sequence file.



'''