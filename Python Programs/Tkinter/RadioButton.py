'''

Tkinter has its own  variables that are slightly different from the python variables

We are going to assign variables to these Radio buttons
Like if someone clicks on that buttons it puts the value into the variable
so that we can take that variable and do operations based on which radio button is clicked

We have to define the Tkinter variables



'''
from tkinter import *

'''
The Function below is to print the value got when the button is clicked
'''


def Clicked(val):
    myLabel = Label(root, text=val)
    myLabel.pack()


root = Tk()

r = IntVar()  # Defining the Tkinter variable
r.get()  # To get the value of the variable at the runtime
# r.set('1')# to set the default value of the variable


Radiobutton(root, text="Option 1", variable=r, value=1).pack()
# To a particular varible a number of buttons are assinged
# based on the selection of butttons the value of the varible is decided
Radiobutton(root, text="Option 2", variable=r, value=2).pack()

# Radiobutton(root,text="Option 1",variable=r,value=1,command= lambda : Clicked(r.get())).pack()
# if this is done then whenever the option is clicked the function is called
# so better to create a button


# Create a submit button
mybtn = Button(root, text="Submit", command=lambda: Clicked(r.get()))
mybtn.pack()

root.mainloop()
