import sqlite3

bankdet = sqlite3.connect("BankDetails.db")
c = bankdet.cursor()


def deposit(req, acc):
    bankdet = sqlite3.connect("BankDetails.db")
    c = bankdet.cursor()
    if acc == req[2]:

        ppin = int(input("Enter Your Pin"))
        if ppin == req[4]:
            dep = int(input('Enter the amount to deposit'))
            req[5] += dep
            print('The balance in Your ACCOUNT is ₹', req[5])

            c.execute("UPDATE details set bal={} WHERE acn={}".format(req[5], acc))


        else:
            print('Icorrect PIN')
    bankdet.commit()
    bankdet.close()


def withdraw(req, acc):
    bankdet = sqlite3.connect("BankDetails.db")
    c = bankdet.cursor()
    if acc == req[2]:

        ppin = int(input("Enter Your Pin"))
        if ppin == req[4]:

            amt = int(input('Enter the amount for Withdrawal'))
            if req[5] >= amt:
                req[5] -= amt
                c.execute("UPDATE details set bal={} WHERE acn={}".format(req[5], acc))

            else:
                print('Insufficient Balance')

            print('The balance in Your ACCOUNT is ₹', req[5])
        else:
            print('Icorrect PIN')
    bankdet.commit()
    bankdet.close()


def find(acc):
    req = []
    bankdet = sqlite3.connect("BankDetails.db")
    c = bankdet.cursor()
    allrec = c.execute("""SELECT * FROM details """).fetchall()

    print(acc)
    for record in allrec:
        if acc == record[2]:
            req = list(record)
            return req


while (1):
    print(
        '\n\n\nWelcome To ABC Bank\n1. Create Account\n2. Deposit\n3. Withdrawal\n4. Change Password\n5. Check Balance\n6. Exit')
    a = int(input())
    if a is 1:
        bankdet = sqlite3.connect("BankDetails.db")
        c = bankdet.cursor()

        name = input('Enter Your Name : ')
        age = int(input('Enter your age : '))
        acn = int(input('Enter Account Number : '))
        min = 1000
        pin = int(input('Please Enter Your 4 Digit Pin : '))
        bal = min
        c.execute("INSERT INTO details VALUES(:name,:age,:acn,:min,:pin,:bal)", {
            'name': name,
            'age': age,
            'acn': acn,
            'min': min,
            'pin': pin,
            'bal': bal
        })
        bankdet.commit()
        print('Account Created')
        bankdet.close()

    elif a is 2:
        acc = int(input('Enter the account number : '))
        req = find(acc)

        if req == None:
            print("Account Number not Exists")
            continue

        req = req
        deposit(req, acc)

    elif a is 3:
        acc = int(input('Enter the account number : '))
        req = find(acc)
        if req == None:
            print("Account Number not Exists")
            continue
        withdraw(req, acc)


    elif a is 4:
        acc = int(input('Enter the account number : '))
        req = find(acc)

        if req == None:
            print("Account Number not Exists")
            continue

        pinn = int(input("Enter your Pin : "))
        if req[4] == pinn:
            confirm = input("Are you sure you want to change your pin ?(Y \ N) : ").capitalize()
            if confirm == 'Y':
                pinr = input("Enter Your pin in Reverse(eg:1234-4321) : ")

                if str(req[4])[::-1] == pinr:
                    newpin1 = int(input("Enter Your new Pin : "))
                    newpin2 = int(input("Confirm Your new Pin : "))
                    if newpin1 == newpin2:
                        bankdet = sqlite3.connect("BankDetails.db")
                        c = bankdet.cursor()
                        c.execute("UPDATE details set pin ={} WHERE acn={}".format(newpin2, acc))
                        bankdet.commit()
                        bankdet.close()
                        print("Pin Changed Successfully!")
                    else:
                        print("New Pin and Confirm Pin are not same\nPlease Try Again")
                        continue
                else:
                    print("Your pin in reverse is not matching\nPlease Try Again")
                    continue
            else:
                continue

        else:
            print("You Have Entered Wrong Pin\nPlease Try Again")


    elif a is 5:
        acc = int(input('Enter the account number : '))
        req = find(acc)

        if req == None:
            print("Account Number not Exists")
            continue

        pinn = int(input("Enter your Pin : "))
        if req[4] == pinn:
            print("Your Account Balance ₹ ", req[5])

        else:
            print("You Have Entered Wrong Pin\nPlease Try Again")
            continue





    elif a is 6:
        exit()
    else:
        continue
