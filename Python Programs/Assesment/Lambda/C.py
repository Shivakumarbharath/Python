'''

. Write a Python program to find if a given string starts with a given character using Lambda.

'''
def Letter(s):
    return lambda x:True if x[0] is s else False
res=Letter('b')
print(res('bengaluru'))
res=Letter('b')
print(res('Karnataka'))