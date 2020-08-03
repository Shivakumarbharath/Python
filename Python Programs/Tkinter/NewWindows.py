from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.title("Main ")


filename = 'StylishAA.jpg'
img = Image.open(filename)
resized_img = img.resize((350, 500))


def New():
    top=Toplevel()
    top.title("Image Opened")
    #To create a new window
    #any functions un the new window is written after creating the window

    label=Label(top,text="Hello This is new Window").pack()
    top.photoimg = ImageTk.PhotoImage(resized_img)
    labelimage = Label(top, image=top.photoimg)
    labelimage.pack()
    btn2=Button(top,text="Exit this",command=top.destroy).pack()
    #here top.quit quits the main window so we use destroy

    '''
    If in a function a variable is not working because it is a local variable
    so make it a global variable
    
    
    '''

btn=Button(root,text="Open Image",command=New).pack()
qbtn=Button(root,text="Exit",command=root.quit).pack()



root.mainloop()