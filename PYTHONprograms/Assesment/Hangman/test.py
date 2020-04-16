from tkinter import *
import random
from Words import Words
import time



def get_word():
    word=random.choice(Words)
    return word#



root=Tk()
def dispTostr(disp):
    string=''
    for e in disp:
        string+=e+'   '
        print(e)
    return string


def repeat(char,word,disp):
    cnt=word.count(char)

    dex=word.index(char)

    disp[word.index(char,dex)] = char
    for i in range(0,cnt-1):
        dex = word.index(char,dex+1)

        disp[word.index(char,dex)] = char
    return disp
#print(dispTostr(repeat('n','dinner',['_','_','_','_','_','_'])))
word=get_word()
print(word)
disp=['_' for k in range(len(word))]
dispL = Label(root, text=dispTostr(disp), padx=5, pady=5, font=('ariel', 12, 'bold'))
dispL.pack()



char=input("enter letter")
dispL = Label(root, text=dispTostr(repeat(char,word,disp)), padx=5, pady=5, font=('ariel', 12, 'bold'))
dispL.pack()





char=input("enter letter")
dispL = Label(root, text=dispTostr(repeat(char,word,disp)), padx=5, pady=5, font=('ariel', 12, 'bold'))
dispL.pack()





char=input("enter letter")

dispL.pack()

root.mainloop()

