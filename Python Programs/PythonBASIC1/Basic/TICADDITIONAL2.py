import sys
from random import randint

X = 1
O = 2
_ = 0
dict = {0: '_', 1: 'X', 2: 'O'}
game = [[_, _, _], [_, _, _], [_, _, _]]


# To print the List
def printlist(list):
    for i in range(3):
        for j in range(3):
            print(dict[list[i][j]], end='\t')
        print('\n')


# To check in Rows if there is winning possibality of player
def rowcheck(list):
    for i in range(0, 3):
        k = 0
        possibality = []
        for j in range(0, 3):
            if list[i][j] == X:
                k += X
            if list[i][j] == O:
                break
            possibality.append(i)
            possibality.append(j)
        if k >= X * 2:
            return possibality

    # else:
    #   columncheck(list)


def columncheck(list):
    for i in range(0, 3):
        k = 0
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
    l = 2
    possibality = []
    for j in range(0, 3):
        if list[j][l] == X:
            k += X
        if list[j][l] == O:
            break
        possibality.append(j)
        possibality.append(l)
        l -= 1
    if k >= X * 2:
        return possibality


# if the player is supposed to win withan entry ,stop the player from winning
def wincheck(newlist):
    i = 0
    while i < len(newlist):
        if game[newlist[i]][newlist[i + 1]] is not X:
            game[newlist[i]][newlist[i + 1]] = O
            return game
        i += 2


# To check the possibality of the computer of winning , if yes the game ends
def compwin(list):
    for i in range(0, 3):
        k = 0
        for j in range(0, 3):
            if list[i][j] == O:
                k += O
            if k == O * 2:
                for l in range(0, 3):
                    if list[i][l] == _:
                        list[i][l] = O

                        k += O
                        if k == O * 3:
                            print('Computer Won')
                        return list

    for j in range(0, 3):
        k = 0
        for i in range(0, 3):
            if list[i][j] == O:
                k += O
            if k == O * 2:
                for l in range(0, 3):
                    if list[l][j] == 0:
                        list[l][j] = O
                        k += O
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
    m = 2
    for i in range(0, 3):
        if list[i][m - i] == O:
            k += O
            print(k)
        if k == O * 2:
            for l in range(0, 3):
                if list[l][m - l] is _:
                    list[l][m - l] = O
                    k += O
                    if k == O * 3:
                        print('Computer Won')
                    return list


def playerwin(X):
    for i in range(0, 2):
        if all(game[i][j] is X for j in range(0, 3)):
            print(name, ' Won')
            exit()
    for i in range(0, 2):
        if all(game[j][i] is X for j in range(0, 3)):
            print(name, ' Won')
            exit()
    if all(game[j][j] is X for j in range(0, 3)):
        print(name, ' Won')
        exit()
    h = 2
    if all(game[j][h - j] is X for j in range(0, 3)):
        print(name, ' Won')
        exit()


name = input('Enter name')
for i in range(5):
    a = int(input('Enter The Row: '))  # row entry
    b = int(input('Enter The colounm: '))  # column entry
    if a > 3 or b > 3:
        print('Wrong Entry of Row or Column\n\nTry Again')
        exit()
    game[a - 1][b - 1] = X  # assign the Entered row and coloumn
    playerwin(X)
    if i == 0:
        c = randint(0, 2)
        d = randint(0, 2)
        while game[c][d] is (X or O):
            c = randint(0, 2)
            d = randint(0, 2)
        game[c][d] = O
        printlist(game)
    elif i is 4:
        printlist(game)
        print(i)
        playerwin(X)
        print('Game Tied')
        exit()
    else:
        d = compwin(game)
        if d is not None:
            printlist(game)
            print('Computer Won\n\nTry Again')
            exit()
        else:
            sim = rowcheck(game) or columncheck(game) or d1(game) or d2(game)
            if sim is None:
                c = randint(0, 2)
                d = randint(0, 2)
                print(c, d)
                while game[c][d] is (O or X):
                    c = randint(0, 2)
                    d = randint(0, 2)
                game[c][d] = O
                printlist(game)
            else:
                b = wincheck(sim)
                if b is None:
                    c = compwin(game)
                    if c is None:
                        c = randint(0, 2)
                        d = randint(0, 2)
                        while game[c][d] is (O or X):
                            c = randint(0, 2)
                            d = randint(0, 2)
                        game[c][d] = O
                        printlist(game)
                    else:
                        printlist(c)
                        print('Computer Won\n\nTry Again')
                        exit()
                else:
                    printlist(b)
playerwin(X)
print('Game Tied\n\nTry Again\n')
