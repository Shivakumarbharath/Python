given = input('Enter the Nucletide')
for char in given:
    if char is not 'A' and char is not 'T' and char is not 'C' and char is not 'G':
        print('invalid')
        break
for i in given:
    if char is not 'A' and char is not 'T' and char is not 'C' and char is not 'G':
        break
    if i is 'C':
        print('G', end='')

    if i is 'G':
        print('C', end='')

    if i is 'A':
        print('U', end='')

    if i is 'T':
        print('A', end='')
