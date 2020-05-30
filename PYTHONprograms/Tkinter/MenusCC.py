from tkinter import *

root=Tk()

#functions
def new():
    pass
def open_files():
    pass
def option1():
    pass
def option2():
    pass




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



root.mainloop()
