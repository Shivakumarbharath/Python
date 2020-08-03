import sys
from random import randint

X = 1
O = 2
_ = 0
dict = {0: '_', 1: 'X', 2: 'O'}
game = [[_, _, _], [_, _, _], [_, _, _]]


def printlist(list):
    for i in range(3):
        for j in range(3):
            print(dict[list[i][j]], end='\t')
        print('\n')


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


def wincheck(newlist):
    i = 0
    while i < len(newlist):
        if game[newlist[i]][newlist[i + 1]] is not X:
            print(newlist[i], newlist[i + 1])
            game[newlist[i]][newlist[i + 1]] = O
            return game
        i += 2


def compwin(list):
    for i in range(0, 3):
        k = 0
        for j in range(0, 3):
            if list[i][j] == O:
                k += O
                print(k)
            if k == O * 2:
                for l in range(0, 3):
                    if list[i][l] == _:
                        list[i][l] = O
                        print(list[i][j])
                        k += O
                        print(k)
                        if k == O * 3:
                            print('Computer Won')
                        return list

    for j in range(0, 3):
        k = 0
        for i in range(0, 3):
            if list[i][j] == O:
                k += O
                print(k)
            if k == O * 2:
                for l in range(0, 3):
                    if list[l][j] == 0:
                        list[l][j] = O
                        k += O
                        print(k)
                        if k == O * 3:
                            print('Computer Won')
                        return list
    k = 0
    for i in range(0, 3):
        if list[i][i] == O:
            k += O
            print(k)
        if k == O * 2:
            for l in range(0, 3):
                if list[l][l] == 0:
                    list[l][l] = O
                    print(list[l][l])
                    k += O
                    print(k)
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
                if list[l][m - l] == 0:
                    list[l][m - l] = O
                    print(list[l][l - m])
                    k += O
                    print(k)
                    if k == O * 3:
                        print('Computer Won')
                    return list


name = input('Enter name')
for i in range(5):
    a = int(input())
    b = int(input())
    game[a - 1][b - 1] = X
    if i == 0:
        c = randint(0, 2)
        d = randint(0, 2)
        while game[c][d] is (X or O):
            c = randint(0, 2)
            d = randint(0, 2)
        game[c][d] = O
        printlist(game)
    else:
        d = compwin(game)
        if d is not None:
            printlist(game)
            print('comp is is not none')
            exit()
        else:
            sim = rowcheck(game) or columncheck(game) or d1(game) or d2(game)
            print(sim)
            print('comp is none')
            if sim is None:
                c = randint(0, 2)
                d = randint(0, 2)
                print(c, d)
                while game[c][d] is (O or X):
                    c = randint(0, 2)
                    d = randint(0, 2)
                    print(c, d)
                game[c][d] = O
                printlist(game)
                print('hiii')
            else:

                b = wincheck(sim)
                if b is None:
                    c = compwin(game)
                    if c is None:
                        c = randint(0, 2)
                        d = randint(0, 2)
                        print(c, d)
                        while game[c][d] is (O or X):
                            c = randint(0, 2)
                            d = randint(0, 2)
                            print(c, d)
                        game[c][d] = O
                        printlist(game)
                        print('compwin is none')
                    else:
                        printlist(c)
                        print('compwin is not none')
                else:
                    printlist(b)
for i in range(0, 2):
    if all(game[i][j] is X for j in range(0, 3)):
        print(name, ' Won')

for i in range(0, 2):
    if all(game[j][i] is X for j in range(0, 3)):
        print(name, ' Won')

if all(game[j][j] is X for j in range(0, 3)):
    print(name, ' Won')
h = 2
if all(game[j][h - j] is X for j in range(0, 3)):
    print(name, ' Won')
else:
    print('Game Tied')
