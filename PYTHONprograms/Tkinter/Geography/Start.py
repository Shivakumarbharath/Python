from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Geography")
root.geometry("400x400")


def Hide_all():
    state_capital_frame.pack_forget()
    state_Frame.pack_forget()

def Hide_children(frame):
    for child in frame.winfo_children():
        child.pack_forget()

def states():
    Hide_all()
    state_Frame.pack(fill=BOTH,expand=1)
    Hide_children(state_Frame)
    myLab=Label(state_Frame,text="States").pack()

def state_capital():
    Hide_all()
    Hide_children(state_capital_frame)
    state_capital_frame.pack(fill=BOTH, expand=1)
    myLab = Label(state_capital_frame, text="States capital").pack()


#create our menu
my_menu=Menu(root)
root.config(menu=my_menu)

#create Geography menu items
states_menu=Menu(my_menu)
my_menu.add_cascade(label="Geography",menu=states_menu)
states_menu.add_command(label="States",command=states)
states_menu.add_command(label="States Capital",command=state_capital)
states_menu.add_separator()
states_menu.add_command(label="Exit",command=root.quit)

state_Frame=Frame(root,width=400,height=400)
state_capital_frame=Frame(root,width=400,height=400)


root.mainloop()