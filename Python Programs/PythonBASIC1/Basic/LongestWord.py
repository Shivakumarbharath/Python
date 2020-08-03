sen = input("Enter a String")

ls = sen.split(' ')
print(ls)
ls2 = []
d = {}
j = 0
for i in ls:  # to calculate the length of only alphabets
    k = 0
    if not d.__contains__(len(i)):
        if i.isalpha() is True:
            d[len(i)] = i
        else:
            for j in i:
                if j.isalpha() is True:
                    k += 1
            if not d.__contains__(k):
                d[k] = i
ls2 = list(d.keys())
print(ls2)
ls2.sort()
lword = d[ls2[len(ls2) - 1]]
print(lword)

'''
#Alternative code

#VIEW CHALLENGE
def LongestWord(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha() or letter.isnumeric():
        nw += letter
      else :
        nw += " "
    return max(nw.split(),key=len)
    
# keep this function call here  
print(LongestWord(input()))

'''
