
from tkinter import *


root=Tk()
def click():
    global label
    label.place_forget()
    label = Label(root, text="new1")
    label.place(relx=.5, rely=.5)
    def part():
        global label
        label.place_forget()
        label = Label(root, text="new2")
        label.place(relx=.5, rely=.5)

    b = Button(root, text="remove Label", command=part)
    b.place(relx=.3, rely=.3)
root.geometry("100x100")
label=Label(root,text="Fuck off")
label.place(relx=.5,rely=.5)
b=Button(root,text="remove Label",command=click)
b.place(relx=.7,rely=.7)
root.mainloop()