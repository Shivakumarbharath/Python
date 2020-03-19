from random import randint
battle=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
a=randint(0,4)
b=randint(0,4)
battle[a][b]='B'
def printt(list):
    for i in range(0,5):
        for j in range(0, 5):
            print(list[i][j],end=' ')
        print('\n')
i=1
trial=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
printt(trial)
#printt(battle)
while i<=5:
    r=int(input('Enter the row'))
    c=int(input('Enter the column'))
    if r>5 or c>5:
        print("The Entered Row or Column does not exist")
        break
    if r-1 is a and c-1 is b:
        print("You won the Game\nYou found the Battle ship")
        break
    else:
        trial[r-1][c-1]='X'
        print('Wrong Answer!!')
        printt(trial)
    i+=1
if i is 6:
    trial[a][b]='B'
    print('Game Over\nTry Again')
    printt(trial)