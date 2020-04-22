from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import messagebox


root=Tk()
def open():
    global my_img

    root.filename = filedialog.askopenfilename(initialdir="E:\Bharath\Python\PYTHONprograms\Tkinterr",
                                               title="MY Viewer Files",
                                               filetypes=(("jpg files", "*.jpg","*.py"), ("all files", '*.*')))

    #to function when clicked
    my_Label=Label(root,text=root.filename).pack()
    print(root.filename)
    my_img=ImageTk.PhotoImage(Image.open(root.filename))
    my_img_lab=Label(image=my_img).pack()


menu1=Menu(root)#a menu inside the root
root.config(menu=menu1)

subm=Menu(menu1)#a menu inside the menu1
menu1.add_cascade(label="file",menu=subm)
subm.add_command(label="exit",command=root.quit)
subm.add_command(label="Open",command=open)

def about():
    messagebox.showinfo("Welcome","Learn Tkinter")


subm2=Menu(menu1)
menu1.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About",command=about)





root.mainloop()