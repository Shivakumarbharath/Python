from tkinter import *
from Words import Words
import random
def get_word():
    word=random.choice(Words)
    return word#
def dispTostr(disp):
    string=''
    for e in disp:
        string+=e+'   '

    return string
#check if any repeataions of char in word
def repeat(char,word,disp):
    cnt=word.count(char)

    dex=word.index(char)

    disp[word.index(char,dex)] = char
    for i in range(0,cnt-1):
        dex = word.index(char,dex+1)

        disp[word.index(char,dex)] = char
    return disp
#Execute


root=Tk()

root.title("Play HANGMAN")
root.iconbitmap('E:\Bharath\Python\PYTHONprograms\Assesment\Hangman\hangman.png')

root.geometry("400x400")
head=Label(root,text="HANGMAN",relief='solid',padx=5,pady=5,font=('ariel',15,'bold'))
head.place(x=150,y=10)
word=get_word()
disp=['_' for k in range(len(word))]


entryL=Label(root,text="Guess the Letter: ",padx=5,pady=5,fg='green',font=("ariel",10))
entryL.place(x=50,y=300)
entryE=Entry(root,width=5,borderwidth=3)
entryE.place(x=160,y=305)
chk=Button(root,text="Check")
chk.place(x=100,y=350)
chances = 6
chan=Label(root,text="Chances: {}".format(chances),padx=5,pady=5,font=('ariel',15,'bold'),fg='green')
chan.place(relx=.95,rely=.785,anchor=E)

def play(word):
    print(word)
    global winL
    disp=['_' for k in range(len(word))]

    dispL = Label(root, text=dispTostr(disp), padx=5, pady=5, font=('ariel', 12, 'bold'))
    dispL.place(relx=.5, rely=.25,anchor =CENTER)

    i=0
    tried = []
    winL = Label(root, text="Start Guessing...", padx=5, pady=5,
                 fg='yellow', font=('ariel', 14, 'bold'))
    winL.place(relx=.5, rely=.45,anchor=CENTER)
    global chances
    chances = 6
    def check(disp):
        global chances
        root.update()

        winL = Label(root, text="Start Guessing ....", padx=5, pady=5,
                     fg='yellow', font=('ariel', 14, 'bold'))


        winL.place(relx=51,rely=10)
        if disp.count('_')<=len(word):
            char=entryE.get()
            entryE.delete(0,END)
            tried.append(char)
            try:


                dispL = Label(root, text=dispTostr(repeat(char,word,disp)), padx=5, pady=5, font=('ariel', 12, 'bold'))
                dispL.place(relx=.5, rely=.25, anchor=CENTER)

                winL.place_forget()
                winL = Label(root, text="Good  Go Ahead ", padx=5, pady=5,
                             fg='Blue', font=('ariel', 14, 'bold'))

                winL.place(x=110, y=155)


                triedL = Label(root, text="You have Entered {} ".format(dispTostr(tried)),fg='brown', padx=5, pady=5, font=('ariel', 12, 'bold'))
                triedL.place(x=50, y=250)
                if disp.count('_') == 0:
                    #print("The Word is", word)
                    chk = Button(root, text="Check", state='disabled')
                    chk.place(x=100, y=350)
                    winL.place_forget()
                    winL=Label(root,text="Congratulation",padx=40, pady=10,fg='Green' , font=('ariel', 14, 'bold'))
                    winL.place(relx=.5,rely=.38,anchor=CENTER)
                    winL2 = Label(root, text="The Word is {} ".format(word),
                                 padx=15, pady=8, fg='blue', font=('ariel', 10, 'bold'))
                    winL2.place(relx=.5, rely=.47,anchor=CENTER)
                    winL3 = Label(root, text="You Have won the Game",
                                 padx=5, pady=5, fg='blue', font=('ariel', 10, 'bold'))
                    winL3.place(relx=.5, rely=.54,anchor=CENTER)
                    #print('You Have won the Game')


            except ValueError:
                triedL = Label(root, text="You have Entered {} ".format(dispTostr(tried)), fg='brown', padx=5, pady=5,
                               font=('ariel', 12, 'bold'))
                triedL.place(x=50, y=250)

                winL = Label(root, text='You hav lost one chance', padx=5,
                             pady=5, bg='Red', font=('ariel', 10, 'bold'))
                winL.place_forget()
                winL.place(x=110, y=160)
                chances -= 1
                chan=Label(root,text="Chances: {}".format(chances),padx=5,pady=5,font=('ariel',15,'bold'),fg='green')
                chan.place(relx=.95,rely=.785,anchor=E)

               # print(man[5-chances])
                if chances==0:
                    chan = Label(root, text="Chances: {}".format(chances), padx=5, pady=5, font=('ariel', 15, 'bold'),
                                 fg='red')
                    chan.place(relx=.95, rely=.785, anchor=E)
                    chk = Button(root, text="Check",state='disabled')
                    chk.place(x=100, y=350)
                    winL = Label(root, text=" Game Over", padx=47, pady=12, fg='red', font=('ariel', 15, 'bold'))
                    winL.place(relx=.5, rely=.38, anchor=CENTER)
                    winL2 = Label(root, text="The Word is {} ".format(word),
                                  padx=40, pady=8, fg='blue', font=('ariel', 10, 'bold'))
                    winL2.place(relx=.5, rely=.47, anchor=CENTER)
                    winL3 = Label(root, text="You Are Out Of Chances",
                                  padx=5, pady=5, fg='blue', font=('ariel', 10, 'bold'))
                    winL3.place(relx=.5, rely=.54, anchor=CENTER)





    chk = Button(root, text="Check",command=lambda :check(disp))
    chk.place(x=100, y=350)

word=get_word()

play(word)





root.mainloop()