'''

 Write a Python program to count the number of characters (character frequency) in a string
'''

chr = input("Enter a string")
dic = {e: chr.count(e) for e in chr}
print(dic)
