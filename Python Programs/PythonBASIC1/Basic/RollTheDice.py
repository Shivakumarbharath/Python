from random import randint

die1 = [1, 2, 3, 4, 5, 6]
die2 = [1, 2, 3, 4, 5, 6]
die3 = [1, 2, 3, 4, 5, 6]
die4 = [1, 2, 3, 4, 5, 6]
loc = []
pl = []
n = int(input('Enter the number of players(min 2 players):'))
print('Game Mode\n 1.Easy (2 dice)\n 2.Medium(3 dice)\n 3.Hard (4 dice) ')
mode = int(input('Your Choice: '))


def roll(name):
    i = 0
    print(name, ' can start to roll the dice')
    pl.append(name)
    if mode is 1:
        while (1):
            a = randint(0, 5)
            b = randint(0, 5)
            print('dice1= ', die1[a], ' dice2= ', die2[b])
            i += 1
            if die1[a] is die2[b]:
                print('Dice are rolled', i, ' times')
                print('Here you go! You got the same number')
                loc.append(i)
                break
    elif mode is 2:
        while (1):
            a = randint(0, 5)
            b = randint(0, 5)
            c = randint(0, 5)
            # input()
            print('dice1= ', die1[a], ' dice2= ', die2[b], 'dice3 = ', die3[c])
            i += 1
            if die1[a] is die2[b] is die3[c]:
                print(i, 'th time')
                print('Here you go! You got the same number')
                loc.append(i)
                break
    elif mode is 3:
        while (1):
            a = randint(0, 5)
            b = randint(0, 5)
            c = randint(0, 5)
            d = randint(0, 5)
            # input()
            print('dice1= ', die1[a], ' dice2= ', die2[b], 'dice3 =', die3[c], 'dice =', die4[d])
            i += 1
            if die1[a] is die2[b] is die3[c] is die4[d]:
                print(i, 'th time')
                print('Here you go! You got the same number')
                loc.append(i)
                break
    else:
        print('Wrong Game Mode')


i = 1
while i <= n:
    name = input('Enter Your Name:  ')
    roll(name)
    i += 1
print(pl[loc.index(min(loc))], ' has Won the Game')
