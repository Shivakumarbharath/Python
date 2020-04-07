from tkinter import *
'''
Create a button widget

Every widget must be created and then put into the window
'''


def myClick():
    label=Label(root,text="Clicked the Button")
    label.pack()


root=Tk()

myButton=Button(root,text="click mee!",command=myClick,bg='blue')#creating a button
#putting into the window
myButton.pack()

'''
inside the button function
the arguments

state=DISABLED this diables the buttun
ex - myButton=Button(text="click mee!",state=DISABLED)

padx and pady - determine the size of the button
ex- myButton=Button(text="click mee!",padx=50,pady=35


TO make the button fuction create a funtion

use command = function name inside the button method
ex-n myButton=Button(root,text="click mee!",command=myClick)
do not use paraenthesis aftere the function name 
there will be a different logic


Changing the colour of te buttons

fg='blue' to make the text on the button blue

bg='blue' - to change the button colour



'''



root.mainloop()