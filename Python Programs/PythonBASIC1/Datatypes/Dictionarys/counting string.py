para = 'AIm for three to five or more sentences per paragraph. Include on each page about two handwritten or three typed paragraphs. Make your paragraphs proportional to your paper. Since paragraphs do less work in short papers, have short paragraphs for short papers and longer paragraphs for longer papers.'
word = 'steerling streeing'


def count(string):
    counts = {}
    for char in string:
        counts[char] = string.count(char)
    return counts


result = count(word)
print(result)
# different approach
# def counting(note)
# counts={}
# for char in note:
#   if char not in note:
#      counts[char]=1
# else:
#    counts[char]=counts[char]+1
# return counts
