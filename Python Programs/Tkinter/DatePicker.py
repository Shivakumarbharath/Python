from tkinter import *
from tkcalendar import *

root = Tk()

root.geometry("400x400")

root.config(bg='Black')

cal = Calendar(root, selectmode='day', year=2020, month=5, date=22)


def grabDate():
    Label(root, text=cal.get_date()).pack()


def grabcal():
    btn2.pack_forget()
    cal.pack(pady=15)


btn2 = Button(root, text="Get calender", command=grabcal)
btn2.pack()

btn = Button(root, text="Get Date", command=grabDate)
btn.pack()

root.mainloop()
