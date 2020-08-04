import turtle  # lib to make simple games
import time
import winsound

t = 0.015
wn = turtle.Screen()  # To make a window to play

wn.title("Lets Play Ping Pong")  # title of the game

wn.bgcolor('Green')  # to have a background colour

wn.setup(width=800, height=600)  # to provide the height of the window  # it has origin at the center

wn.tracer(0)  # stops the window from updating

# items in the game
# Paddle A
paddle_a = turtle.Turtle()  # to create an object
paddle_a.speed(0)  # speed of the animation
paddle_a.shape('square')  # shape of the paddle  # default 20 x 20 pixels
paddle_a.color('yellow')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # Turtle draw a line as moving
paddle_a.goto(-360, 0)

# paddle B
paddle_b = turtle.Turtle()  # to create an object
paddle_b.speed(0)  # speed of the animation
paddle_b.shape('square')  # shape of the paddle  # default 20 x 20 pixels
paddle_b.color('yellow')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # Turtle draw a line as moving
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()  # to create an object
ball.speed(0)  # speed of the animation
ball.shape('square')  # shape of the paddle  # default 20 x 20 pixels
ball.color('yellow')
ball.penup()  # Turtle draw a line as moving so to stop it
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('White')
pen.penup()
pen.goto(0, 260)
pen.hideturtle()  # no need of viewing the object
pen.write('Player A : 0  Player B : 0', align='center', font=("Courier", 15, 'normal'))


# functions

def paddle_a_up():
    y = paddle_a.ycor()  # returns the current y coordinate

    y += 20  # calculate the y to be added

    paddle_a.sety(y)  # set the new y


def paddle_a_down():
    y = paddle_a.ycor()  # returns a y coordinate

    y -= 20  # calculate the y to be added

    paddle_a.sety(y)  # set the new y


def paddle_b_up():
    y = paddle_b.ycor()  # returns a y coordinate

    y += 20  # calculate the y to be added

    paddle_b.sety(y)  # set the new y


def paddle_b_down():
    y = paddle_b.ycor()  # returns a y coordinate

    y -= 20  # calculate the y to be added

    paddle_b.sety(y)  # set the new y


# kewboard binding

wn.listen()  # to listen for keyboard input and bind the keyboard

wn.onkeypress(paddle_a_up, 'w')  # this tells when key 'w ' is pressed perform the function paddle a up
# to listen for keyboard input and bind the keyboard
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, 'Up')

wn.onkeypress(paddle_b_down, 'Down')
# Main game loop # Every Game will have a main loop

while True:
    wn.update()  # every time the loop runs it updates the screen

    # mall movment

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        # mac sound import os for linux and mac
        # os.system("afplay 'music name'& " )  music file should be in same folder & is used to avoid delay

        # linux sound - instead oof afplay use aplay

        # import winsound in windows

        # winsound.Playsound("music name",winsound.SND_ASYNC)  #same as '&'
        pen.clear()
        pen.write('Player A : %(a)d  ,Player B : %(b)d ' % {'a': score_a, 'b': score_b}, align='center',
                  font=("Courier", 15, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)

        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A : %(a)d  ,Player B : %(b)d ' % {'a': score_a, 'b': score_b}, align='center',
                  font=("Courier", 15, 'normal'))

    # ball and paddle collusion

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    time.sleep(t)
