str1 = input('Enter a string')
vowels = ['a', 'e', 'i', 'o', 'u']
vowels2 = ['A', 'E', 'I', 'O', 'U']
i = 0
j = 0
for k in range(0, len(str1)):
    for j in range(0, len(vowels)):
        if str1[k] == vowels[j] or str1[k] == vowels2[j]:
            i += 1

if i == len(vowels):
    print('Accepted')
else:
    print('Not accepted')

# char = ('A' or 'a') and ('E'or 'e') and ('I' or 'i') and ('O' or 'o') and ('U' or 'u')
# if 'A' or 'a' in str1 and ('E'or 'e') in str1 and ('I' or 'i') in str1 and ('O' or 'o') in str1 and ('U' or 'u') in str1:
#     print('Accepted')
# else:
#     print('Not Accepted')
