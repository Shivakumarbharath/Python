from tkinter import *

root=Tk()
root.geometry('500x400')

#entry=Entry(root)
#entry.grid(row=0,column=0,padx=5,pady=5)

lst=[]
for row in range(0,3):
    for colunm in range(0,4):
        lst.append(Entry(root))
        lst[-1].grid(row=row,column=colunm,padx=5,pady=5)


root.mainloop()