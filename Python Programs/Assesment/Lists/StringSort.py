'''

 Split a list based on first character of word

'''

Word = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
        'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

sortlist = sorted(Word, key=lambda x: x[0])

for i, x in enumerate(sortlist):
    if sortlist[i - 1][0] != x[0]:
        print('from the letter ', x[0])
    print(x)
