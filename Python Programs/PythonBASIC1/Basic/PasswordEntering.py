#get pass works only in the terminal and not in console
from getpass import getpass
import time

psw=getpass("enter your password",{'*'})
time.sleep(1)
print(psw)

