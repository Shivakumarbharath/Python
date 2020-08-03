from tkinter import *
from PIL import ImageTk,Image
from random import randint
root=Tk()
root.title("Geography")
root.geometry("500x600")


def check():
    s=answer.get().lower()
    if s == our_states[r]:
        #print(s,our_states[r])
        states()
        c=Label(state_Frame,text="Correct answer",padx=5,pady=5,bg='White')
        c.pack()
        #states()
    else:
        w=Label(state_Frame, text="Wrong answer! try again", padx=5, pady=5,bg='White')
        w.pack()

def Hide_all():
    state_capital_frame.pack_forget()
    state_Frame.pack_forget()

def Hide_children(frame):
    for child in frame.winfo_children():
        child.pack_forget()

def states():
    global resized_img, r, answer,our_states
    Hide_all()
    state_Frame.pack(fill=BOTH,expand=1)
    Hide_children(state_Frame)
    #create list of state names
    our_states=['andhra pradesh','delhi','goa','gujrat','karnataka','kerala','madhya pradesh','maharashtra','rajastan','tamil nadu','telangana','west bengal']

    #generate random number

    r=randint(0,len(our_states)-1)

    filename = 'states/'+our_states[r]+'.jpg'
    state_image = Image.open(filename)
    resized_img = state_image.resize((400, 400))
    root.photoimg = ImageTk.PhotoImage(resized_img)

    #create our state images
    show_state=Label(state_Frame,image=root.photoimg)
    show_state.pack()

    #create button to randomize

    random_button=Button(state_Frame,text="pass",command=states,padx=5,pady=5).pack()

    #entery
    answer=Entry(state_Frame,bd=2)
    answer.pack()

    #check button
    answer_check=Button(state_Frame,text="Submit",command=check,padx=5,pady=6)
    answer_check.pack()
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

state_Frame=Frame(root,width=400,height=400,bg='white')
state_capital_frame=Frame(root,width=400,height=400)


root.mainloop()