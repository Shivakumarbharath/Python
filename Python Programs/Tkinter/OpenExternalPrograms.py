from tkinter import *
from tkinter import filedialog
import os #to open the application

root=Tk()

root.geometry("300x300")
def open_diloge():
    ext=filedialog.askopenfilename()#to get the path of the file
    lab.config(text=ext)
    os.system('"{}"'.format(ext))#to open the file
btn=Button(root,text="Open external",command=open_diloge)
btn.pack()

lab=Label(root,text='')
lab.pack()


root.mainloop()