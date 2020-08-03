class Bank:
    def __init__(self):
        self.name = input('Enter You Name')
        self.age = int(input('Enter your age'))
        self.acn = int(input('Enter Account Number'))
        self.min = 1000
        self.pin = int(input('Please Enter Your 4 Digit Pin:'))
        self.bal = self.min


    def depost(self):

        self.ppin = int(input("Enter Your Pin"))
        if self.ppin == self.pin:
            self.dep = int(input('Enter the amount to deposit'))
            self.bal += self.dep
            print('Your Balance is', self.bal)
        else:
            print('Incorrect PIN')

    def withdraw(self):
        self.ppin = int(input("Enter Your Pin"))
        if self.ppin == self.pin:
            self.wd = int(input('Enter the amount for Withdrawal'))
            if self.wd < self.bal:
                self.bal -= self.wd
                print('The balance in Your ACCOUNT is ', self.bal)
            else:
                print('Insufficient Balance')
        else:
            print('Incorrect PIN')


acs = []
while (1):
    print('Welcome To ABC Bank\n 1.Create Account\n2.deposit\n3.withdrawal\n4.exit')
    a = int(input())
    if a is 1:
        acs.append(Bank())
    elif a is 2:
        acc = int(input('Enter the account number'))
        for i in range(0, len(acs)):
            if acc == acs[i].acn:
                print(acs[i].acn)
                acs[i].depost()

    elif a is 3:
        acc = int(input('Enter the account number'))
        for i in range(0, len(acs)):
            if acc == acs[i].acn:
                acs[i].withdraw()

    elif a is 4:
        exit()