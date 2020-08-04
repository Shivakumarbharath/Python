from tkinter import *
from tkinter import colorchooser

root = Tk()
root.geometry('300x300')


def colour():
    colour = colorchooser.askcolor()
    Label(root, text=colour, bg=colour[1]).pack()
    print(colour)


cBtn = Button(root, text="Colour", command=colour).pack()

root.mainloop()
