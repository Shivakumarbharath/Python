from tkinter import *

root = Tk()

E = Entry(root, width=50, font=('ariel', 6))
E.pack(padx=5, pady=5)


def Click():
    hello = 'Hello  ' + E.get()
    E.delete(0, END)
    l = Label(root, text=hello)
    l.pack()


btn = Button(root, text="Name", command=Click)
btn.pack()

root.mainloop()
