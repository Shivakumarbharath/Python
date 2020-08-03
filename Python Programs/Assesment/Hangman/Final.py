from tkinter import *
import random
from tkinter import messagebox

sports = ('arena', 'athletic', 'backboard', 'backhand', 'batter (baseball)', 'baseball',
          'basketball', 'bench', 'catcher', 'champion', 'championship', 'coach', 'competitive',
          'defense', 'doubles', 'dribble', 'dugout', 'fan',
          'field goal', 'finish line', 'football', 'forehand', 'goalkeeper', 'goalpost')
air_Travel = (
'aisle', 'arrival', 'baggage', 'board', 'bulkhead', 'carry-on', 'coach', 'cockpit', 'connection', 'crew', 'customs',
'declare',
'departure', 'duty-free',
'gate', 'itinerary', 'jet engine', 'jet lag', 'jumbo jet', 'landing', 'lavatory', 'luggage', 'one-way', 'overbook',
'oxygen mask')
environment = ('aquifer', 'atmosphere', 'biodegradable', 'biodiversity', 'carbon dioxide', 'carbon monoxide',
               'carcinogen', 'climate', 'coal', 'compost (noun)', 'compost (verb)', 'conservation', 'conservationist',
               'contaminant', 'contamination', 'deforestation', 'disposable', 'diversity', 'ecology', 'ecosystem',
               'emission',
               'endangered', 'energy', 'environment', 'environmentalist', 'erosion', 'extinct', 'extinction',
               'fossil fuel', 'geothermal')

family = ('mother', 'mom', 'father', 'dad', 'parent', 'children', 'son', 'daughter', 'sister', 'brother',
          'grandmother', 'grandfather', 'grandparent', 'grandson', 'granddaughter', 'grandchild', 'aunt',
          'uncle', 'niece', 'nephew', 'cousin', 'husband', 'wife', 'sister-in-law', 'brother-in-law', 'mother-in-law',
          'father-in-law', 'partner')
jobs_professions = ('accountant', 'actor', 'actress', 'architect', 'artist', 'attorney', 'banker', 'bartender',
                    'barber', 'bookkeeper', 'builder', 'businessman', 'businesswoman',
                    'businessperson', 'butcher', 'carpenter', 'cashier', 'chef', 'coach',
                    'dentist', 'designer', 'developer', 'dietician', 'doctor', 'economist',
                    'editor', 'electrician', 'engineer')

law = (
'arrest', 'accuse', 'acquit', 'adjourn', 'adoption', 'alibi', 'alimony', 'appeal', 'appeal', 'attorney', 'bankrupt',
'bribe',
'brief', 'case', 'common-law', 'contract', 'copyright' 'court', 'criminal (adjective)', 'custody', 'damages',
'death sentence', 'defend')

emotions = (
'acceptance', 'admiration', 'affection', 'aggravation', 'anger', 'anguish', 'anxiety', 'attraction', 'boredom',
'caution',
'certainty', 'compassion', 'confidence', 'confusion', 'contentment', 'courage', 'curiosity', 'defeat', 'defiance',
'delight',
'dependence', 'depression', 'desire', 'disappointment', 'dislike', 'dismay', 'distress', 'embarrassment', 'enthusiasm',
'envy')

body_parts = (
'ankle', 'arch', 'arm', 'armpit', 'beard', 'breast', 'calf', 'cheek', 'chest', 'chin', 'earlobe', 'elbow', 'eyebrow',
'eyelash', 'eyelid', 'face', 'finger', 'forearm', 'forehead', 'gum', 'heel', 'hip', 'index finger', 'jaw', 'knee',
'knuckle',
'leg', 'lip', 'mouth', 'mustache')

non_count_nouns = (
'advice', 'agriculture', 'air', 'anger', 'attention', 'chaos', 'clothing', 'courage', 'dirt', 'equipment', 'fun',
'furniture',
'garbage', 'homework', 'housework', 'information', 'jewelry', 'luck', 'luggage', 'mail', 'news', 'patience',
'permission',
'pollution', 'progress', 'research', 'scenery', 'slang', 'smoke', 'soccer')

health = ('ache', 'allergy', 'antihistamine', 'appetite', 'aspirin', 'bandage', 'bandage', 'blood', 'bone', 'broken',
          'bronchitis',
          'bruise', 'bruise', 'cast', 'clinic', 'cold', 'contagious', 'cough', 'crutch', 'cut', 'decongestant',
          'diarrhea', 'dizzy',
          'fever', 'first aid', 'flu', 'headache', 'hives', 'indigestion', 'infection')

college = ('campus', 'community college', 'course', 'credit', 'degree', 'dorm', 'enroll', 'exam', 'faculty', 'fail',
           'financial aid',
           'fraternity', 'gpa', 'graduate', 'graduate', 'instructor', 'lecture', 'major', "master's degree",
           'matriculate', 'notebook', 'notes',
           'pass', 'phd', 'postgraduate', 'prerequisite', 'professor', 'quiz', 'goa')

Catagory = [sports, air_Travel, environment, family, jobs_professions, law, emotions, body_parts, non_count_nouns,
            health, college]

Catagory_text = {sports: 'Sports', air_Travel: "Air Travel", environment: "Environment", family: "Family",
                 jobs_professions: "Jobs or Professions", law: "Law", emotions: "Emotions", body_parts: "Body Parts",
                 non_count_nouns: "Non-Count-Nouns",
                 health: "Health", college: "College Life"}


def get_word():
    global catagory, disp
    cat = random.choice(Catagory)
    word = random.choice(cat)
    catagory = Catagory_text[cat]
    # print(catagory,'13')
    disp = ['_' for k in range(len(word))]
    return word


def dispTostr(disp):
    string = ''
    for e in disp:
        string += e + '   '

    return string


# check if any repeataions of char in word
def repeat(char, word, disp):
    cnt = word.count(char)

    dex = word.index(char)

    disp[word.index(char, dex)] = char
    for i in range(0, cnt - 1):
        dex = word.index(char, dex + 1)

        disp[word.index(char, dex)] = char
    return disp


# Execute

def openwindow():
    global root, head, word, disp, entryE, entryL, chk, chances, chan, pla, qbtn, catagory
    root = Tk()

    root.title("Play HANGMAN")
    root.iconbitmap('E:\Bharath\Python\PYTHONprograms\Assesment\Hangman\85370_game_hangman.ico')

    root.geometry("400x400")
    head = Label(root, text="HANGMAN", relief='solid', padx=5, pady=5, font=('Times', 15, 'bold italic underline'))
    head.place(x=150, y=10)
    # word = get_word()
    # disp = ['_' for k in range(len(word))]

    entryL = Label(root, text="Guess the Letter: ", padx=5, pady=5, fg='green', font=("ariel", 12, 'italic'))
    entryL.place(x=27, y=298)
    entryE = Entry(root, width=5, borderwidth=3)
    entryE.place(x=160, y=305)
    chk = Button(root, text="Check")
    chk.place(x=100, y=350)
    chances = 10
    chan = Label(root, text="Chances: {}".format(chances), padx=5, pady=5, font=('ariel', 15, 'bold'), fg='green')
    chan.place(relx=.95, rely=.785, anchor=E)

    # To Play Again
    pla = Button(root, text="Play Again", state='disabled')
    pla.place(x=160, y=350)
    # to quit
    qbtn = Button(root, text="Quit", command=root.quit)
    qbtn.place(x=300, y=350)


'''
winL = Label(root, text="", padx=5, pady=5, fg='yellow', font=('ariel', 14, 'bold'))
winL.place(relx=51, rely=10)
winL2 = Label(root, text='', padx=15, pady=8, fg='blue', font=('ariel', 10, 'bold'))
winL2.place(relx=.5, rely=.47, anchor=CENTER)
winL3 = Label(root, text="", padx=5, pady=5, fg='blue', font=('ariel', 10, 'bold'))
winL3.place(relx=.5, rely=.54, anchor=CENTER)
'''


def play(word):
    global chances
    global winL2
    global winL
    global winL3
    global dispL
    hintLabel = Label(root, text="Hint : {}".format(catagory), bg='orange')
    hintLabel.place(x=50, y=55)

    pla = Button(root, text="Play Again", state='disabled')
    pla.place(x=160, y=350)
    # print(word)
    disp = ['_' for k in range(len(word))]
    dispL = Label(root, text=' ')
    dispL.place(relx=.1, rely=.1)

    dispL = Label(root, text=dispTostr(disp), padx=5, pady=5, font=('ariel', 12, 'bold'))
    dispL.place(relx=.5, rely=.25, anchor=CENTER)
    '''
    winL = Label(root, text='                       ')
    winL.place(relx=.1, rely=.1)
    winL2 = Label(root, text=' ')
    winL2.place(relx=.1, rely=.1)
    winL3 = Label(root, text=' ')
    winL3.place(relx=.1, rely=.1)
    '''
    i = 0
    tried = []
    winL = Label(root, text="Start Guessing...", padx=5, pady=5,
                 fg='yellow', font=('ariel', 14, 'bold'))
    winL.place(relx=.5, rely=.45, anchor=CENTER)

    chances = 10

    def check(disp):
        global winL, w, w, w2, w3
        global winL2
        global winL3
        global chances
        char = entryE.get()
        if char is '':
            messagebox.showinfo("Empty Check", "Guess the Letter: This Block cannot Be Empty")
            chk = Button(root, text="Check", command=lambda: check(disp))
            chk.place(x=100, y=350)



        else:

            winL = Label(root, text="Start Guessing ....", padx=5, pady=5,
                         fg='yellow', font=('ariel', 14, 'bold'))
            winL.place(relx=51, rely=10)

            if disp.count('_') <= len(word):
                char = entryE.get()
                entryE.delete(0, END)
                tried.append(char)
                try:

                    dispL = Label(root, text=dispTostr(repeat(char, word, disp)), padx=5, pady=5,
                                  font=('ariel', 12, 'bold'))
                    dispL.place(relx=.5, rely=.25, anchor=CENTER)

                    winL.configure(text="Good  Go Ahead ")
                    root.update_idletasks()

                    # winL.place_forget()
                    winL = Label(root, text="Good  Go Ahead ", padx=5, pady=5,
                                 fg='Blue', font=('ariel', 14, 'bold'))

                    winL.place(x=110, y=155)

                    triedL = Label(root, text="You have Entered {} ".format(dispTostr(tried)), fg='brown', padx=5,
                                   pady=5, font=('ariel', 12, 'bold'))
                    triedL.place(x=35, y=250)
                    if disp.count('_') == 0:
                        # print("The Word is", word)
                        chk = Button(root, text="Check", state='disabled')
                        chk.place(x=100, y=350)
                        winL.place_forget()

                        winL = Label(root, text="Congratulation", padx=40, pady=10, fg='Green',
                                     font=('ariel', 14, 'bold'))
                        winL.place(relx=.5, rely=.38, anchor=CENTER)

                        winL2 = Label(root, text=" The Word is {} ".format(word),
                                      padx=18, pady=8, fg='blue', font=('ariel', 10, 'bold'))
                        winL2.place(relx=.5, rely=.47, anchor=CENTER)
                        winL3 = Label(root, text="You Have won the Game",
                                      padx=5, pady=5, fg='blue', font=('ariel', 10, 'bold'))
                        winL3.place(relx=.5, rely=.54, anchor=CENTER)
                        pla = Button(root, text="Play Again", command=playagain)
                        pla.place(x=160, y=350)

                        qbtn = Button(root, text="Quit", command=root.quit)
                        qbtn.place(x=300, y=350)

                        # print('You Have won the Game')


                except ValueError:
                    triedL = Label(root, text="You have Entered {} ".format(dispTostr(tried)), fg='brown', padx=5,
                                   pady=5,
                                   font=('ariel', 12, 'bold'))
                    triedL.place(x=35, y=250)

                    winL = Label(root, text='You hav lost one chance', padx=5,
                                 pady=5, bg='Red', font=('ariel', 10, 'bold'))
                    winL.place_forget()
                    winL.place(x=110, y=160)
                    chances -= 1
                    chan = Label(root, text=" Chances: {}".format(chances), padx=5, pady=5, font=('ariel', 15, 'bold'),
                                 fg='green')
                    chan.place(relx=.95, rely=.785, anchor=E)

                    # print(man[5-chances])
                    if chances == 0:
                        chan = Label(root, text=" Chances: {}".format(chances), padx=5, pady=5,
                                     font=('ariel', 15, 'bold'),
                                     fg='red')
                        chan.place(relx=.95, rely=.785, anchor=E)
                        chk = Button(root, text="Check", state='disabled')
                        chk.place(x=100, y=350)
                        winL = Label(root, text=" Game Over", padx=47, pady=12, fg='red', font=('ariel', 15, 'bold'))
                        winL.place(relx=.5, rely=.38, anchor=CENTER)
                        winL2 = Label(root, text="The Word is {} ".format(word),
                                      padx=40, pady=8, fg='blue', font=('ariel', 10, 'bold'))
                        winL2.place(relx=.5, rely=.47, anchor=CENTER)
                        winL3 = Label(root, text="You Are Out Of Chances",
                                      padx=5, pady=5, fg='blue', font=('ariel', 10, 'bold'))
                        winL3.place(relx=.5, rely=.54, anchor=CENTER)
                        pla = Button(root, text="Play Again", command=playagain)
                        pla.place(x=160, y=350)

                        qbtn = Button(root, text="Quit", command=root.quit)
                        qbtn.place(x=300, y=350)

    chk = Button(root, text="Check", command=lambda: check(disp))
    chk.place(x=100, y=350)


def playagain():
    root.destroy()
    openwindow()
    play(get_word())


openwindow()
word = get_word()
# print(word,'232')
play(word)

#
# response = messagebox.askyesno("Do You Want to Play Again?")
# if response == 1:
#     word = get_word()
#     play(word)
# else:
#     exit()


root.mainloop()
