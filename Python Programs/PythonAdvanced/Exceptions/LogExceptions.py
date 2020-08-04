import logging

logging.basicConfig(filename="MyFIle", level=logging.INFO)  # all logging errors are viewd  in log files

try:
    f = open("Exceptions", 'w')
    try:  # Nested Exceptions

        a, b = [int(x) for x in input("Enter Two numbers").split()]

    except ValueError:
        print("Two numbers to be enterd")
        a, b = [int(x) for x in input("Enter Two numbers").split()]

    logging.info("Division in progress")  # can view only in log file
    c = a / b
    f.write("The Answer is %.2f" % c)
    print("The Answer is %.2f" % c)

except ZeroDivisionError:  # When the error is zero division this block gets executed
    print("Division by zero not allowed")
    logging.error("Division by Zero")

else:  # this is used after try and except to execute when no error is raised
    print("You have enntered a non zero number")

finally:  # whatever may be the execution above but this gets executed after the above execution
    f.close()
    print("File Closed")

print(a)

print(b)
