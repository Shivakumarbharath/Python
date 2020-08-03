para='AIm for three to five or more sentences per paragraph.\n Include on each page about two handwritten or three typed paragraphs.\n Make your paragraphs proportional to your paper.\n Since paragraphs do less work in short papers, have short paragraphs for short papers and longer paragraphs for longer papers.'
f=open("book.txt",'w')
f.write(para)
f=open("book.txt",'r')
text=f.read()
print(text)
