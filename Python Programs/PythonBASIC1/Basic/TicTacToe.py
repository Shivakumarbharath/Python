
from random import randint
X=1
O=2
_=0
dict={0:'_',1:'X',2:'O'}
game=[[_,_,_],[_,_,_],[_,_,_]]
#To print the List
def printlist(list):
    for i in range(3):
        for j in range(3):
            print(dict[list[i][j]],end='\t')
        print('\n')
# To check in Rows if there is winning possibality of player
def rowcheck(list):
    for i in range(0,3):
        k=0
        print('row')
        possibality=[]
        for j in range(0,3):

            if list[i][j]==X:
                k+=X
            if list[i][j]==O:
                break
            possibality.append(i)
            possibality.append(j)
        if k>=X*2:
            return possibality

    #else:
     #   columncheck(list)
def columncheck(list):

    for i in range(0,3):
        k = 0
        print('coulumn')
        possibality = []
        for j in range(0, 3):

            if list[j][i] == X:
                k += X
            if list[j][i] == O:
                break
            possibality.append(j)
            possibality.append(i)
        if k >= X * 2:
            return possibality
def d1(list):
    k = 0
    print('dia1')
    possibality = []
    for j in range(0, 3):

        if list[j][j] == X:
            k += X
        if list[j][j] == O:
            break
        possibality.append(j)
        possibality.append(j)
    if k >= X * 2:
        return possibality
def d2(list):
    k = 0
    l=2
    print('dia 2')
    possibality = []
    for j in range(0, 3):

        if list[j][l] == X:
            k += X
        if list[j][l] == O:
            break
        possibality.append(j)
        possibality.append(l)
        l-=1
    if k >= X * 2:
        return possibality
#if the player is supposed to win withan entry ,stop the player from winning
def wincheck(newlist):
    i=0
    while i<len(newlist):
        if game[newlist[i]][newlist[i+1]] is not X:
            game[newlist[i]][newlist[i+1]]=O
            return game
        i += 2
#To check the possibality of the computer of winning , if yes the game ends
def compwin(list):
    for i in range(0,3):
        k = 0
        for j in range(0, 3):
            if list[i][j]==O:
                k +=O
            if k == O * 2:
                for l in range(0,3):
                    if list[i][l]==_:
                        list[i][l]=O

                        k+=O
                        if k == O * 3:
                            print('Computer Won')
                        return list

    for j in range(0,3):
        k = 0
        for i in range(0, 3):
            if list[i][j]==O:
                k +=O
            if k == O * 2:
                for l in range(0,3):
                    if list[l][j]==0:
                        list[l][j]=O
                        k+=O
                        if k == O * 3:
                            print('Computer Won')
                        return list
    k = 0
    for i in range(0, 3):
        if list[i][i] == O:
            k += O
        if k == O * 2:
            for l in range(0, 3):
                if list[l][l] == 0:
                    list[l][l] = O

                    k += O
                    if k == O * 3:
                        print('Computer Won')
                    return list
    k = 0
    m=2
    for i in range(0, 3):
        if list[i][m-i] == O:
            k += O
            print(k)
        if k == O * 2:
            for l in range(0, 3):
                if list[l][m-l] is _:
                    list[l][m-l] = O
                    k += O
                    if k == O * 3:
                        print('Computer Won')
                    return list
def playerwin(Y,name):
    for i in range(0,2):
        if all(game[i][j] is Y for j in range(0,3)):
            printlist(game)
            print(name ,' Won')
            exit()
    for i in range(0,2):
        if all(game[j][i] is Y for j in range(0,3)):
            printlist(game)
            print(name ,' Won')
            exit()
    if all(game[j][j] is Y for j in range(0,3)):
        printlist(game)
        print(name, ' Won')
        exit()
    h=2
    if all( game[j][h-j] is Y  for j in range(0,3)):
        printlist(game)
        print(name, ' Won')
        exit()
def play(player,M):
    print(player+"'s"+' turn')
    choice=int(input('Enter the place'))
    if choice == 1:
        a=3
        b=1
    elif choice ==2:
        a=3
        b=2
    elif choice == 3:
        a=3
        b=3
    elif choice == 4:
        a=2
        b=1
    elif choice == 5:
        a=2
        b=2
    elif choice == 6:
        a=2
        b=3
    elif choice == 7:
        a=1
        b=1
    elif choice==8:
        a=1
        b=2
    elif choice == 9:
        a=1
        b=3
    else:
        print('Wrong Input else')
        play(player,M)
    '''
    if game[a-1][b-1] is not _:
        print('Wrong Input if')
        play(player, M)'''
    game[a-1][b-1]=M

def computer():
    name=input('Enter Your Name')
    for i in range(5):
        # a=int(input('Enter The Row: ')) #row entry
        # b=int(input('Enter The colounm: '))#column entry
        # if a>3 or b>3:
        #     print('Wrong Entry of Row or Column\n\nTry Again')
        #     exit()

        # if game[a-1][b-1]==O:
        #     print('Wrong entry\nPlace not empty')
        #     continue
        # game[a-1][b-1]=X  #assign the Entered row and coloumn

        play(name,X)
        playerwin(X,name)
        if i == 0 :
            c=randint(0,2)
            d=randint(0,2)
            while game[c][d] is O or game[c][d] is X:
                c = randint(0, 2)
                d = randint(0, 2)
            game[c][d]=O
            printlist(game)
        elif i is 4:
            playerwin(X,name)
            print('Game Tied')
            exit()
        else:
            d= compwin(game)
            if d is not None:
                printlist(game)
                print('Computer Won\n\nTry Again')
                exit()
            else:
                sim = rowcheck(game) or columncheck(game) or d1(game) or d2(game)
                if sim is None:
                    c = randint(0, 2)
                    d = randint(0, 2)
                    print(c,d)
                    while game[c][d] is O or game[c][d] is X:
                        c = randint(0, 2)
                        d = randint(0, 2)
                    game[c][d] = O
                    printlist(game)
                else:
                    b=wincheck(sim)
                    if b is None:

                        c=compwin(game)
                        if c is None:
                            sim=d2(game) or d1(game) or columncheck(game) or rowcheck(game)
                            b1=wincheck(sim)
                            if b1 == None:
                                c = randint(0, 2)
                                d = randint(0, 2)
                                while game[c][d] is O or game[c][d] is X:
                                    c = randint(0, 2)
                                    d = randint(0, 2)
                                game[c][d] = O
                                printlist(game)
                            else:
                                printlist(game)
                        else:
                            printlist(c)
                            print('Computer Won\n\nTry Again')
                            exit()
                    else:
                        printlist(b)
    playerwin(X,name)
    print('Game Tied\n\nTry Again\n')

def p12():
    name1=input('Enter Player 1 Name')
    name2=input('Enter Player 2 Name')
    for i in range(5):
        if i == 4:
            playerwin(X, name2)
            playerwin(O, name1)
            play(name1,O)
            playerwin(X, name2)
            playerwin(O, name1)
            printlist(game)
            print('Game Tied')
            exit()
        play(name1,O)
        playerwin(O, name1)
        playerwin(X, name2)
        printlist(game)

        play(name2,X)
        playerwin(X, name2)
        playerwin(O, name1)
        printlist(game)



while(1):
    print("Welcome to MY game\n\nSelect Mode\n1.ONE Player\n2.TWO Players\n3.Exit")
    gm=int(input())
    if gm == 1:
        computer()
    elif gm ==2:
        p12()
    elif gm == 3:
        exit()
    else:
        print('Incorrect Mode')
        exit()
    print('Game Tied')