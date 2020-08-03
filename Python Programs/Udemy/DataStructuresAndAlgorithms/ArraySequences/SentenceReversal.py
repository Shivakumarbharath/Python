'''

Actual Algorithm for reversal of sentences

1.seperate the words in the sentence
2.Reverse the sequence
3.join it


'''




string='Hi my name is Bharath '
#In python all are possible in one line
final=' '.join(reversed(string.split()))
print(final)

#In manual

#To split the words
def Split(string):

    #To store the splitted words
    words=[]
    #to make sure thast no spaces are the in words
    spaces=[' ']
    #Iterator
    i=0

    length=len(string)

    while i<length:
        if string[i] not in spaces:
            word_start=i

        while string[i] not in spaces:
            i+=1

        words.append(string[word_start:i])

        i+=1

    return words


#to reverse in a list
def reverse(lst):
    new_lst=[]
    length=len(lst)-1
    while length>=0:
        new_lst.append(lst[length])
        length-=1
    return new_lst


#to Join the string
final=' '.join(reverse(Split(string)))

print(final)

