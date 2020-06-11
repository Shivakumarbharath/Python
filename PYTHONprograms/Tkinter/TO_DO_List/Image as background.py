from tkinter import *
from PIL import Image, ImageTk


from tkinter import colorchooser

IMAGE_PATH = 'background.jpg'
WIDTH, HEIGTH = 500, 500

root = Tk()
root.geometry('{}x{}+100+100'.format(WIDTH, HEIGTH))

canvas = Canvas(root, width=WIDTH, height=HEIGTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=NW, image=img)


def colour():

    colour = colorchooser.askcolor()
    bg = colour[1]
    cBtn.config(bg=bg)
    button.config(bg=bg)
    lab.config(bg=bg)
    print(colour[1])



# Put a tkinter widget on the canvas.
button = Button(root, text="Start",relief=GROOVE)
cBtn=Button(root,text="Colour",command=colour,relief=GROOVE)
button_window = canvas.create_window(150, 200, anchor=NW, window=button)
cBtn_window=canvas.create_window(200,200,anchor=NW, window=cBtn)

lab=Label(root,text='the colour')
lab_wind=canvas.create_window(10,200,anchor=NW,window=lab)

root.mainloop()