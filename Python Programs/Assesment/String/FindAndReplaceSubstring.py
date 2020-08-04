'''


. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''

Srt1 = input("Enter the Sentence")

inot = Srt1.find('not')

ipoor = Srt1.find('poor')

if (inot < ipoor) and (inot >= 0) and (
        ipoor >= 0):  # (inot >= 0) and (ipoor>=0) - because if find is false it returns -1
    Srt1 = Srt1.replace(Srt1[inot:ipoor + 4], 'good')

print(Srt1)
