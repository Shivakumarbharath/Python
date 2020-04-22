from tkinter import *

root=Tk()

days=["Mon","Tues",'Wednes','Thurs',"Fri","satur"]
days=[day+"Day" for day in days]
print(days)

Day=StringVar()
Day.set("Select Day")
d=OptionMenu(root,Day,*days)
d.pack()
def click():
    lab=Label(root,text=Day.get())
    lab.pack()

btn=Button(root,text="Result",command=click)
btn.pack()


root.mainloop()