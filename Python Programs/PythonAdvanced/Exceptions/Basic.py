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
    f = open("Exceptions", 'w')
    try:  # Nested Exceptions

        a, b = [int(x) for x in input("Enter Two numbers").split()]

    except ValueError:
        print("Two numbers to be enterd")
        a, b = [int(x) for x in input("Enter Two numbers").split()]

    c = a / b
    f.write("The Answer is %.2f" % c)
    print("The Answer is %.2f" % c)

except ZeroDivisionError:  # When the error is zero division this block gets executed
    print("Division by zero not allowed")

else:  # this is used after try and except to execute when no error is raised
    print("You have entered a non zero number")

finally:  # whatever may be the execution above but this gets executed after the above execution
    f.close()
    print("File Closed")

print(a)

print(b)
