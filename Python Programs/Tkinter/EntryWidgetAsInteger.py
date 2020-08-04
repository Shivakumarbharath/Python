from tkinter import *
from PIL import Image, ImageTk


def Check():
    try:
        k = int(enter.get())
        answer.config(text=str(k) + ' is a number')
    except ValueError:
        tst = enter.get()
        enter.delete(0, END)
        answer.config(text="{} is not a Number".format(tst))


root = Tk()
root.geometry('300x300')

label = Label(root, text="Enter a number : ")
label.pack()

enter = Entry(root)  # ,show='*')
enter.pack()

btn = Button(root, text="check", command=Check)
btn.pack()

answer = Label(root, text='')
answer.pack()

root.mainloop()
