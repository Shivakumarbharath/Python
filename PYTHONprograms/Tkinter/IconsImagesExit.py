from tkinter import *
from PIL import ImageTk,Image

filename = 'StylishAA.jpg'
img = Image.open(filename)
resized_img = img.resize((350, 500))

root = Tk()

root.title("Know To Code")
root.iconbitmap('E:\Bharath\Python\PYTHONprograms\Tkinter\Calculator.ico')

root.photoimg = ImageTk.PhotoImage(resized_img)
labelimage = Label(root, image=root.photoimg)
labelimage.pack()


#the below works if no resizing

# my_img=ImageTk.PhotoImage(Image.open(img location))
# lab=Label(image=my_img)
# lab.pack()


ext=Button(root,text='Exit',command=root.quit)
ext.pack()




root.mainloop()


'''
filename = 'bell.jpg'
img = Image.open(filename)
resized_img = img.resize((200, 100))

root = tk.Tk()
root.photoimg = ImageTk.PhotoImage(resized_img)
labelimage = tk.Label(root, image=root.photoimg)
labelimage.pack()

'''