'''
There was a teacher in small town who loves coding
and he wants to create a program which prints out the whole
multiplicaion table of an entered number for his students.
write program


'''
# my solution
n = int(input("Enter the number of table ? : "))
for i in range(1, 16):
    print("{} x {} = {}".format(n, i, n * i))
