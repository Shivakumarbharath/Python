'''
n=4
         1
      2 1 1 2
   3 2 1   1 2 3
4 3 2 1     1 2 3 4
   3 2 1   1 2 3
      2 1 1 2
         1
#spaces before numbers 9,6,3 - 2n+(n-3)===3n-3----9
#spaces between numbers 1,3,5  n-1 odd numbers



n=5
            1
         2 1 1 2
      3 2 1   1 2 3
   4 3 2 1     1 2 3 4
5 4 3 2 1       1 2 3 4 5
   4 3 2 1     1 2 3 4
      3 2 1   1 2 3
         2 1 1 2
            1

#spaces before numbers 12,9,6,3  3n-3        if n=6  2n+3
#spaces between numbers 1,3,5,7 n-1 odd numbers
'''

#spaces before numbers 9,6,3
#spaces between numbers 1,3,5
#This logic works only till number 9
n=int(input("Enter a Number Between 2-9"))  #to take the number of rows
numSpaces=3*n-3 #number ofspaces bfore the number starts
spaces=list(range(2,n*(n+2),2))[:n-2]#spaces between the numbers
print(' '*(numSpaces),end='1 ')#the first number
numSpaces-=3
k=0
for i in range(2,n+1):
    print()
    print(' '*(numSpaces),end='')#spaces before the number
    num=range(1,i+1)#to print the numbers in a singel  row
    for e in num[::-1]:#to print the numbers in a singel  row
        print(e,end=' ')
    if i !=2:#to print spaces between the numbers
        print(' '*spaces[k],end='')
        k+=1
    for e in num:#to print the numbers in same Row
        print(e,end=' ')
    numSpaces-=3
print()
spaces=spaces[::-1][1:]+[0]#reversing the number of spaces as above
numSpaces+=6#after the abovse for loop it becomes -3
k=0
for i in range(2,n+1)[::-1][1:]:
    print(' ' * (numSpaces), end='')
    num = range(1, i + 1)
    for e in num[::-1]:
        print(e, end=' ')
    if spaces[k]!=1:
       print(' ' * spaces[k], end='')
    k+=1
    for e in num:
        print(e, end=' ')
    print()
    numSpaces += 3
print(' '*(numSpaces),end='1 ')
