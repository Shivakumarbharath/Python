from tkinter import *
from PIL import Image,ImageTk

root =Tk()
root.geometry('300x300')

login='login.jpg'
img=Image.open(login)
img=img.resize((120,50))


root.photimg=ImageTk.PhotoImage(img)
#LoginIMG=Label(root,image=root.photimg)
#LoginIMG.place(x=66,y=30)0

btn=Button(root,image=root.photimg,bd=0)
btn.pack()

root.mainloop()