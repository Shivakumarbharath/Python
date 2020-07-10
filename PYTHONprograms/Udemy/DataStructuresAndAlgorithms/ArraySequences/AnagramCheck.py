'''

Problem
Given two strings ,check to see if they are anagram.
an anagram is when the two strings can be written with the exact same letters
to get a different words


Algorithim 1
1.Replace spaces with null in both the strings and lower case all the letters
2.check the lengths of both the strings
3.check if every letter in the string 2 is present in string 1

Algorithm 2
1.Replace spaces with null in both the strings and lower case all the letters
2.sort the strings
3.check if equal

'''


st1='public relations'
st2='crap built on lies'

def anagram(st1,st2):

    #1.Replace spaces with null in both the strings
    changed_st1=st1.replace(' ','').lower()
    changed_st2=st2.replace(' ','').lower()

    #2.Check the length of both the strings
    if len(changed_st1)!=len(changed_st2):
        return False

    #3.check every letter in string 2 is presrnt in string 1
    for e in changed_st2:
        if e in changed_st1:
            continue
        else:
            return False

    return True

print(anagram(st1,st2))






