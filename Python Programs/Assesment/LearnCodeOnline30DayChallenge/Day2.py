'''
make a pattern
        * *
        * *
      * * * *
      * * * *
    * * * * * *
    * * * * * *     4-6  5-8 6-10 7-12
  * * * * * * * *
  * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *


'''

n = 6
bspace = 2 * n - 2
start = 2
for i in range(0, n):
    for j in range(2):
        print(' ' * bspace, end='')
        print('* ' * start)
        print()
    start += 2
    bspace -= 2
