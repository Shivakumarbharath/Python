import random

point = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
var = ['Rock', 'Paper', 'Scissors']
user_choice = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

comp_score = 0
player_score = 0

while (comp_score <= 4) and (player_score <= 4):
    comp = random.choice(var)
    try:
        player = int(input("1.Rock\n2.Paper\n3.Scissors\nMake Choice : "))
    except ValueError:
        print('You Didnt make the choice\n\n')
        continue

    if player > 3:
        print('Make an appropriate choice\n')
        continue
    print('\nComputer :{}'.format(comp))
    if point[comp] == user_choice[player]:
        player_score += 1
        print('\n\nYou won\n\nYour Score : {}\nComputer Score : {}\n'.format(player_score, comp_score))

    elif comp == user_choice[player]:
        print('\n Draw\n')

    else:
        comp_score += 1
        print('\n\nYou Lost\n\nYour Score : {}\nComputer Score : {}\n'.format(player_score, comp_score))

print('Your Score : {}\nComputer Score : {}'.format(player_score, comp_score))
