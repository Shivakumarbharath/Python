from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry('600x600')
# create a canvas widget

w = 400
h = 400
x = w // 2
y = h // 2

my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=30)

file = 'E:\Bharath\Python\PYTHONprograms\Tkinter\Viewer\destination_1.jpg'
img = Image.open(file)
imgres = img.resize((160, 160))

root.photoimg = ImageTk.PhotoImage(imgres)

can = my_canvas.create_image(0, 0, anchor=NW, image=root.photoimg)


def move(event):
    global imgres
    root.photoimg = ImageTk.PhotoImage(imgres)

    can = my_canvas.create_image(event.x, event.y, image=root.photoimg)

    mylab.config(text='x={} y={}'.format(event.x, event.y))


my_canvas.bind("<B1-Motion>", move)

mylab = Label(root, text='')
mylab.pack()

root.mainloop()
