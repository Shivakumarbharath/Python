'''
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'''

sample = input("Enter")

for i in range(len(sample)):
    if i != 1:
        if sample[0] == sample[i]:
            sample = sample.replace(sample[i], '$')

print(sample)

'''
Efficient and alternative

  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]


'''
