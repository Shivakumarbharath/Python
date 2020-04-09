'''

 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character
re same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2

'''

lst=input().split(',')

def FirstLast(str):
    if len(str)>=2:
        if str[0]==str[-1]:
            return 1
        else:
            return 0
    else:
        return 0


res=list(map(FirstLast,lst))

print(sum(res))


'''

Alternative

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))

'''