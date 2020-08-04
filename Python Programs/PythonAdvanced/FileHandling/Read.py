import os, sys  # for checking a file

if os.path.isfile("myfile.txt"):

    f = open("myfile.txt", "r")
    s = f.read()
    print(s)
    f.close()

else:
    print("File does not exists")
