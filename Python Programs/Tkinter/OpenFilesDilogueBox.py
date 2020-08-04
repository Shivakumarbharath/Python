from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()


# to open the files as it is


def open():
    global my_img

    root.filename = filedialog.askopenfilename(initialdir="E:\Bharath\Python\PYTHONprograms\Tkinter\Viewer",
                                               title="MY Viewer Files",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", '*.*')))

    # to function when clicked
    my_Label = Label(root, text=root.filename).pack()
    print(root.filename)
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_lab = Label(image=my_img).pack()


btn = Button(root, text="Open Files", command=open).pack()

root.mainloop()
