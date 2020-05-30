from tkinter import *
from PIL import ImageTk,Image
root =Tk()

root.geometry('600x600')
#create a canvas widget

w=400
h=400
x=w//2
y=h//2

my_canvas=Canvas(root,width=w,height=h,bg='white')
my_canvas.pack(pady=30)


file='E:\Bharath\Python\PYTHONprograms\Tkinter\Viewer\destination_1.jpg'
img=Image.open(file)
imgres=img.resize((160,160))

root.photoimg=ImageTk.PhotoImage(imgres)

can=my_canvas.create_image(0,0,anchor=NW,image=root.photoimg)

#using letters
def press(event):
    x,y=0,0
    if event.char=='a':x=-10
    if event.char == 'd': x = 10
    if event.char == 'w': y = -10
    if event.char == 's': y = 10

    my_canvas.move(can,x,y)

root.bind("<Key>",press)



root.mainloop()