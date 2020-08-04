from tkinter import *

root = Tk()
root.geometry("250x250")
vertical = Scale(root, from_=0, to=500)
vertical.pack()
# vertical.place(x=210,y=0)

horiz = Scale(root, from_=0, to=500, orient="horizontal")
horiz.pack()


# horiz.place(x=0,y=210)

def Resize():
    # print(str(horiz.get())+"x"+str(vertical.get()))
    root.geometry(str(horiz.get()) + "x" + str(vertical.get()))


buttn = Button(root, text="Resize", command=Resize).pack()

root.mainloop()
