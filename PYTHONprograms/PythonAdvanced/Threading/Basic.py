'''

The Python virtual machine by default works on the main() thread
this is callesd single threading.

to make best use of processer and to improve the performance of the application
we can create multiple threads that can execute in parallel and make best use of prossecor and
best user experiencewe use multi threading

Multiple can be done in 3 ways :-
1. Using Function
    We first define a function
    create an object
        t = Thread(target=FunctionName,args)
    then invoke
        t.start() - when you do that python virtual machine will create a new thread
        that will run in parallel with main thread .

2. Extending a thread class
    thread class is from python threading module
    we will import that module
    extend the thread class
        class MyThread(Thread)
    step 2- override  the run()



'''