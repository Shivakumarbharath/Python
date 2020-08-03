'''
e=Entry(root,width=20,bg='blue')

e=Entry(root,width=20,bg='blue',borderwidth=6)


e.get()# to retrive the information entered

e.insert(0,"Enter your name")#insertes text inside the input field

'''

from tkinter import *

root = Tk()


def myClick():
    label = Label(root, text=e.get())
    label.pack()


e = Entry(root, width=20, borderwidth=6)
e.pack()
e.insert(0, "Enter your name")  # insertes text inside the input field
myButton = Button(root, text="click mee!", command=myClick, bg='blue')  # creating a button
# putting into the window
myButton.pack()

root.mainloop()
