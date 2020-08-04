'''
Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.

Examples
Given that:
  - "A" char code is: 65
  - "a" char code is: 97

counterpartCharCode("A") ➞ 97

counterpartCharCode("a") ➞ 65
'''

char = 'gdgf'


def counterpartCharCode(char):
    if char.isalpha:

        if char.isupper():
            return ord(char.lower())

        if char.islower():
            return ord(char.upper())

    else:
        return ord(char)
