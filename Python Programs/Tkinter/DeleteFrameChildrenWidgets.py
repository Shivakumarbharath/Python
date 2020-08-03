from tkinter import *

root = Tk()
root.geometry('300x300')



#functions
def new():
    file_new_frame.pack(fill=BOTH, expand=1)
def open_files():
    mylab=Label(file_new_frame,text="click").pack()
def option1():
    Label(root,text="Option1").pack()
def option2():
    pass

def copy():
    edit_new_frame.pack(fill=BOTH)#, expand=1)

def cut():
    hide_all_frames()
    Label(root,text="You Clicked cut").pack()

def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()#to destroy all the children in the frame
    edit_new_frame.pack_forget()
    file_new_frame.pack_forget()

my_menu=Menu(root)
root.config(menu=my_menu)#to root-use my_menu as menu

#create a menu item

#creating sub menus
file_menu=Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
#Adding items in sub menu File
file_menu.add_command(label="New",command=new)
file_menu.add_separator()#separates with a line
file_menu.add_separator()

file_menu.add_command(label="open",command=open_files)
file_menu.add_separator()
file_menu.add_command(label="exit",command=root.quit)

option_menu=Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)

option_menu.add_command(label="option1",command=option1)
option_menu.add_command(label="option2",command=option2)

edit_menu=Menu(root)
my_menu.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="cut",command=cut)
edit_menu.add_command(label="copy",command=copy)


#create frames
file_new_frame=Frame(root,width=400,height=400,bg='black',)
edit_new_frame=Frame(root,width=300,height=200,bg='yellow')




root.mainloop()