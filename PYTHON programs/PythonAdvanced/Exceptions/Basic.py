'''
Exception is a runtime error

Exceptions will cause:
1. Abnormal Termination of program
2. Informal /unfriendly information to the end user
3. Improper shut down of the resources


In python Exception is a class

4 parts
Try :
Except  :
else:
finally: this code is executed finally whatever may be the exeption above
'''

try:
    f=open("Exceptions",'w')
    try:

        a,b=[int(x)for x in input("Enter Two numbers").split()]

    except ValueError:
        print("Two numbers to be enterd")
        a, b = [int(x) for x in input("Enter Two numbers").split()]


    c=a/b
    f.write("The Answer is %.2f" %c)
    print("The Answer is %.2f" %c)

except ZeroDivisionError:
    print("Division by zero not allowed")

finally:
    f.close()
    print("File Closed")


print(a)


print(b)

