from tkinter import *

root=Tk()
root.geometry('300x300')
#using config all the attributes for any widget
def config():
    l.configure(text="configured")


l=Label(root,text="HI original text")
l.pack()

b=Button(root,text="click to change",command=config)
b.pack()


root.mainloop()
