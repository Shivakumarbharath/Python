from Words import Words
import random

man = ['''
                @-------|
                |       |
                |       
                |      
                |       
                |      


    ''',
    '''
                @-------|
                |       |
                |       O
                |      
                |       
                |      


    '''
    '''
                 @-------|
                 |       |
                 |       O
                 |       |
                 |       |
                 |       
 
 
    ''',
    '''
                 @-------|
                 |       |
                 |       O
                 |      \|
                 |       |
                 |       
 
 
    ''',
    '''
                 @-------|
                 |       |
                 |       O
                 |      \|/
                 |       |
                 |       
 
 
    ''',
    '''
                 @-------|
                 |       |
                 |       O
                 |      \|/
                 |       |
                 |      / 
 
 
    ''',
    '''
                 @-------|
                 |       |
                 |       O
                 |      \|/
                 |       |
                 |      / \  
 
 
    '''
      ]
#get a Word from Words.py
def get_word():
    word=random.choice(Words)
    return word#
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
def play(word):

    disp=['_' for k in range(len(word))]
    chances =6
    print(*disp)
    tried=[]
    i=0
    while disp.count('_')<=len(word):
        char=input("Enter a letter")
        tried.append(char)
        try:
            disp=repeat(char,word,disp)
            print("You have Tried",*tried)
            if disp.count('_') == 0:
                print("The Word is", word)
                print('You Have won the Game')
                exit()

        except ValueError:
            print("You Have lost one chance")
            print("You have Tried", *tried)

            chances-=1
            print(man[5-chances])
            if chances==0:
                print("The Word is", word)
                print("Game Over")
                exit()

        print(*disp)

while True:
    print("Hello !\n\nWelcome to Hangman")
    word=get_word()
    print(man[0])
    play(word)
    if input("Want to Play Again (Y/N)").upper()=='Y':
        word = get_word()
        play(word)
    else:
        print("Had Nice Fun \n\nCome Back Again")
        break