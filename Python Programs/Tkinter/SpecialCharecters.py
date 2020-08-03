from tkinter import *

root = Tk()

my_Label = Label(root, text="42" + u"\u270c", font=('ariel', 35)).pack()

_Label = Label(root, text="42" + u"\u2b50", font=('ariel', 35)).pack()

root.mainloop()
