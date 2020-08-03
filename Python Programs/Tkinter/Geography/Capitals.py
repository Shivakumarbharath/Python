from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title("Geography")
root.geometry("500x600")


def check():
    s = answer.get().lower()
    if s == our_states[r]:
        # print(s,our_states[r])
        states()
        c = Label(state_Frame, text="Correct answer", padx=5, pady=5, bg='White')
        c.pack()
        # states()
    else:
        w = Label(state_Frame, text="Wrong answer! try again", padx=5, pady=5, bg='White')
        w.pack()


def Hide_all():
    # hide all frames
    state_capital_frame.pack_forget()
    state_Frame.pack_forget()


def Hide_children(frame):
    # hide all children of the frame
    for child in frame.winfo_children():
        child.pack_forget()


def capital_check(capital, choice):
    # to check if answer is correct

    if capital == choice:

        # state_capital()
        # result = Label(state_capital_frame, text="Correct Answer", bg='White')
        # result.pack()

        # if correct update the result
        result.configure(text="Correct Answer")
        result.update()
        # activate the nxt button so the next question is asked
        nxtBtn['state'] = 'active'

    else:
        # if result.winfo_exists()==1:
        #   result.destroy()
        # result = Label(state_capital_frame, text="Wrong Answer", bg='White')
        # result.pack()

        # update if wrong
        result.configure(text="Wrong Answer\n The correct answer is {}".format(capital))
        result.update()


def states():
    # globalize required variables
    global resized_img, r, answer, our_states
    # hide frames
    Hide_all()
    Hide_children(state_Frame)
    state_Frame.pack(fill=BOTH, expand=1)

    # create list of state names
    our_states = ['andhra pradesh', 'delhi', 'goa', 'gujrat', 'karnataka', 'kerala', 'madhya pradesh', 'maharashtra',
                  'rajastan', 'tamil nadu', 'telangana', 'west bengal']

    # generate random number

    r = randint(0, len(our_states) - 1)

    # resize the selected image
    filename = 'states/' + our_states[r] + '.jpg'
    state_image = Image.open(filename)
    resized_img = state_image.resize((400, 400))
    root.photoimg = ImageTk.PhotoImage(resized_img)

    # create our state images
    show_state = Label(state_Frame, image=root.photoimg)
    show_state.pack()

    # create button to randomize
    random_button = Button(state_Frame, text="pass", command=states, padx=5, pady=5).pack()

    # entery
    answer = Entry(state_Frame, bd=2)
    answer.pack()

    # check button
    answer_check = Button(state_Frame, text="Submit", command=check, padx=5, pady=6)
    answer_check.pack()
    # myLab=Label(state_Frame,text="States").pack()


def state_capital():
    # hide frames
    Hide_all()

    state_capital_frame.pack(fill=BOTH, expand=1)
    Hide_children(state_capital_frame)
    our_states = ['andhra pradesh', 'delhi', 'goa', 'gujrat', 'karnataka', 'kerala', 'madhya pradesh',
                  'maharashtra', 'rajastan', 'tamil nadu', 'telangana', 'west bengal']
    # dictionary of states and capitals
    capitals = {
        our_states[0]: 'Vizag',
        our_states[1]: 'Itself is a capital',
        our_states[2]: 'Panaji',
        our_states[3]: 'GandhiNagar',
        our_states[4]: 'Bengaluru',
        our_states[5]: 'Trivendram',
        our_states[6]: 'Bhopal',
        our_states[7]: 'Mumbai',
        our_states[8]: 'Jaipur',
        our_states[9]: 'Chennai',
        our_states[10]: 'Hydrabad',
        our_states[11]: 'Kolkota',

    }
    # create a random number
    r = randint(0, len(our_states) - 1)
    # select and  resize the image
    filename = 'states/' + our_states[r] + '.jpg'
    state_image = Image.open(filename)
    resized_img = state_image.resize((400, 400))
    root.photoimg = ImageTk.PhotoImage(resized_img)
    # selectese states
    state = our_states[r]
    # create our state images
    show_state = Label(state_capital_frame, image=root.photoimg)
    show_state.pack()
    Label(state_capital_frame, text="Capital of this State is :", bg='white').pack()
    # store the capital of the selected state
    capital = capitals[state]
    # to create options
    # gather all capitals
    all_capitals = list(capitals.values())
    # removse the capital from the caitals list as it is already stored
    capital = all_capitals.pop(all_capitals.index(capital))
    # create option list
    options = [all_capitals.pop(randint(0, len(all_capitals) - 1)) for i in range(0, 3)]
    # take another random option
    # for i in range(0,3):
    #     options.append(all_capitals.pop(randint(0,len(all_capitals)-1)))
    options.append(capital)

    # shuffle it
    random.shuffle(options)
    # create radio buttons
    radio_opt = StringVar()
    radio_opt.set(None)
    for option in options:
        Radiobutton(state_capital_frame, text=option, variable=radio_opt, value=option, bg='white', bd=3).pack(anchor=W)

    # button to submit the answer
    ans_btn = Button(state_capital_frame, text="Submit", command=lambda: capital_check(capital, radio_opt.get()))
    ans_btn.pack()

    # to get the next question
    global nxtBtn
    nxtBtn = Button(state_capital_frame, text="Next", command=state_capital, state=DISABLED)
    nxtBtn.place(relx=0.8, rely=0.8)

    # to view the result
    global result
    result = Label(state_capital_frame, text="                                  ", bg='White')
    result.place(relx=0.6, rely=0.9)

    #
    # myLab = Label(state_capital_frame, text="States capital").pack()


# create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# create Geography menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="States Capital", command=state_capital)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

# create frames
state_Frame = Frame(root, width=400, height=400, bg='white')
state_capital_frame = Frame(root, width=400, height=400, bg='white')

root.mainloop()
