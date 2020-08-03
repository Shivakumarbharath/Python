'''

If there are Several Radio Buttons We cannot write it 10 Times
So we will use a loop to create Radio Buttons

'''

from tkinter import *


def Clicked(val):
    myLabel = Label(root, text=val)
    myLabel.pack()


share = [
    "Reliance", "TATA", "MRF", "Nestle"

]
root = Tk()

r = StringVar()  # Defining the Tkinter variable
r.get()  # To get the value of the variable at the runtime
r.set(None)

for e in share:
    Radiobutton(root, text=e, variable=r, value=e).pack(anchor=W)  # anchor to be in line

mybtn = Button(root, text="Submit", command=lambda: Clicked(r.get()))
mybtn.pack()

root.mainloop()
