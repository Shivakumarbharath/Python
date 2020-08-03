from tkinter import *
from PIL import ImageTk,Image
from random import randint
root=Tk()
root.title("Geography")
root.geometry("500x500")


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
    #create list of state names
    our_states=['andhra pradesh','delhi','goa','gujrat','karnataka','kerala','madhya pradesh','maharashtra','rajastan','tamil nadu','telangana','west bengal']

    #generate random number
    r=randint(0,len(our_states)-1)
    global resized_img
    filename = 'states/'+our_states[r]+'.jpg'
    state_image = Image.open(filename)
    resized_img = state_image.resize((400, 400))
    root.photoimg = ImageTk.PhotoImage(resized_img)

    #create our state images
    show_state=Label(state_Frame,image=root.photoimg)
    show_state.pack()

    #create button to randomize

    random_button=Button(state_Frame,text="change",command=states).pack()
    #myLab=Label(state_Frame,text="States").pack()

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