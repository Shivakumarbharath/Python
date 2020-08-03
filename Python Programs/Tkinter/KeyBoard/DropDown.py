from tkinter import *
from tkinter import ttk

root=Tk()
def select(event):
    Label(root,text=combo.get()).pack()

option=[
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

clicked=StringVar()
clicked.set(option[0])

combo=ttk.Combobox(root,value= option)
combo.pack()
combo.bind("<<ComboboxSelected>>",select)#when selected
combo.current(0)
#combo.bind("<<ComboboxSelected>>",select)


drop=OptionMenu(root,clicked,*option,command=select)
drop.pack()


#btn=Button(root,text="Select",command=select)
#btn.pack()

root.mainloop()