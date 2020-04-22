from tkinter import *

root=Tk()

var=StringVar()
var2=StringVar()
# var.set("Off")
# var2.set("Off")

c=Checkbutton(root,text="Chech this Box",variable=var,onvalue="On",offvalue="Off")
c.pack()
c.deselect()


d=Checkbutton(root,text="Check 2",variable=var2,onvalue="On",offvalue="Off")
d.pack()
d.deselect()


lab=Label(root,text=var.get())
lab.pack()
def click():
    lab = Label(root, text=var.get())
    lab.pack()

    lab2 = Label(root, text=var2.get())
    lab2.pack()

btn=Button(root,text="Text",command=click)
btn.pack()

root.mainloop()