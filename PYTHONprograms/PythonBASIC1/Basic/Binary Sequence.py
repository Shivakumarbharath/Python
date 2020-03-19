from sys import stdin, stdout
n =int(stdin.readline())
while n>0:
    A=[int(i) for i in stdin.readline().split()]
    if (A[2]+A[3] == A[0]*A[1]):
        stdout.write('Yes'+'\n')
    else :
        stdout.write('No'+'\n')
    n-=1