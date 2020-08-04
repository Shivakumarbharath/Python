'''
 Write a Python program to wrap a given string into a paragraph of given width. Go to the editor
Sample Output:
Input a string: The quick brown fox.
Input the width of the paragraph: 10
Result:
The quick
brown fox.
'''

sst = input("Enter the string")
n = int(input("enter the size of parahgraph"))
for i in range(1, len(sst) + 1):
    print(sst[i - 1], end='')
    if i % n == 0:
        print()
        continue
