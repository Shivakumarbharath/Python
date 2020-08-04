# to acces the main thread

import threading

a = threading.current_thread().getName()  # gives current name of thread

print("current thread is :", a)

# to compare with amin thread

if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("some other")
