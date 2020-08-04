from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("X-O-X")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player_1name = Entry(root, textvariable=p1, bd=5)
player_1name.grid(row=1, column=1, columnspan=8)
player_2name = Entry(root, textvariable=p2, bd=5)
player_2name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0


def disable_button():
    Button_1.configure(state=DISABLED)
    Button_2.configure(state=DISABLED)
    Button_3.configure(state=DISABLED)
    Button_4.configure(state=DISABLED)
    Button_5.configure(state=DISABLED)
    Button_6.configure(state=DISABLED)
    Button_7.configure(state=DISABLED)
    Button_8.configure(state=DISABLED)
    Button_9.configure(state=DISABLED)


def btnClick(buttons):
    global bclick, flag, pa, player_1name, player_2name, playerb
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + "Wins"
        pa = p1.get() + "Wins"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1


    else:
        messagebox.showinfo("Tic-Tac-Toe", "Button Already Clicked")


def checkForWin():
    if (Button_1["text"] == 'X' and Button_2["text"] == "X" and Button_3["text"] == "X" or
            Button_4["text"] == 'X' and Button_5["text"] == "X" and Button_6["text"] == "X" or
            Button_7["text"] == 'X' and Button_8["text"] == "X" and Button_9["text"] == "X" or
            Button_1["text"] == 'X' and Button_4["text"] == "X" and Button_7["text"] == "X" or
            Button_2["text"] == 'X' and Button_5["text"] == "X" and Button_8["text"] == "X" or
            Button_3["text"] == 'X' and Button_6["text"] == "X" and Button_9["text"] == "X" or
            Button_1["text"] == 'X' and Button_5["text"] == "X" and Button_9["text"] == "X" or
            Button_3["text"] == 'X' and Button_5["text"] == "X" and Button_7["text"] == "X"

    ):
        disable_button()
        messagebox.showinfo("Tic-Tac-Toe", pa)

    elif (flag == 8):
        messagebox.showinfo("Tic-Tac-Toe", "It was a Tie")
        disable_button()


    elif (Button_1["text"] == 'O' and Button_2["text"] == 'O' and Button_3["text"] == 'O' or
          Button_4["text"] == 'O' and Button_5["text"] == 'O' and Button_6["text"] == 'O' or
          Button_7["text"] == 'O' and Button_8["text"] == 'O' and Button_9["text"] == 'O' or
          Button_1["text"] == 'O' and Button_4["text"] == 'O' and Button_7["text"] == 'O' or
          Button_2["text"] == 'O' and Button_5["text"] == 'O' and Button_8["text"] == 'O' or
          Button_3["text"] == 'O' and Button_6["text"] == 'O' and Button_9["text"] == 'O' or
          Button_1["text"] == 'O' and Button_5["text"] == 'O' and Button_9["text"] == 'O' or
          Button_3["text"] == 'O' and Button_5["text"] == 'O' and Button_7["text"] == 'O'

    ):
        disable_button()
        messagebox.showinfo("Tic-Tac-Toe", pa)

    # else :
    #     messagebox.showinfo("Tic-Tac-Toe","It was a Tie")


lab1 = Label(root, text="Player 1")
lab1.grid(row=1, column=0)

lab = Label(root, text="Player 2")
lab.grid(row=2, column=0)


def MainPlay():
    global Button_1, Button_3, Button_2, Button_4, Button_5, Button_6, Button_7, Button_8, Button_9

    Button_1 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_1))
    Button_1.grid(row=3, column=0)

    Button_2 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_2))
    Button_2.grid(row=3, column=1)

    Button_3 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_3))
    Button_3.grid(row=3, column=2)

    Button_4 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_4))
    Button_4.grid(row=4, column=0)

    Button_5 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_5))
    Button_5.grid(row=4, column=1)

    Button_6 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_6))
    Button_6.grid(row=4, column=2)

    Button_7 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_7))
    Button_7.grid(row=5, column=0)

    Button_8 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_8))
    Button_8.grid(row=5, column=1)

    Button_9 = Button(root, text=' ', bg="gray", height=4, width=8, command=lambda: btnClick(Button_9))
    Button_9.grid(row=5, column=2)


MainPlay()


def Again():
    player_1name.delete(0, END)
    player_2name.delete(0, END)
    MainPlay()


menu1 = Menu(root)  # a menu inside the root
root.config(menu=menu1)
menu1.add_cascade(label="Play Again", command=Again)
menu1.add_cascade(label="Exit", command=root.quit, )

root.mainloop()
