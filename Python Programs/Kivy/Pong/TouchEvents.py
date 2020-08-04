from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty  # similar to datatypes
from kivy.vector import Vector  # to get the vector postion
from kivy.clock import Clock
import random


class PongPaddle(Widget):
    # on_touch_down()-when our fingers/mouse touches the screen
    # on_touch_up()-when we lift of our fingers off the screen
    # on_touch_move()-when we drag our fingers or the mouse
    pass


class PongBall(Widget):  # all the classes created will be a rule in .kv file
    # to create the animation
    # since these work also on different languages its type of variable has to be given
    velocity_x = NumericProperty(0)  # 0 initial value
    velocity_y = NumericProperty(0)
    # to reference both the variables we use this method
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # latest position = cuurrent velocity +current poition
    # method to move
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

        '''
        Animating process
        Clock method(update(),60fps)
        Update()to call the move function and and to add other stuff

        move function is to move the ball

        '''


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(random.randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # y bounce
        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1

        # x bounce
        if (self.ball.x < 0) or (self.ball.x > self.width - 50):
            self.ball.velocity_x *= -1

    def on_touch_move(self, touch):
        if touch.x < self.width / 4:
            self.player1.center_y = touch.y

        if touch.x > self.width * 3 / 4:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


# to run the app
PongApp().run()

'''
#.kv file

<PongBall>
    size:50,50
    canvas:
        Ellipse:
            pos:self.pos
            size:self.size

<PongPaddle>
    size:25,200
    canvas:
        Rectangle:
            pos:self.pos
            size: self.size

<PongGame>
    ball:Pong_ball
    player1:paddle_left
    player2:paddle_right
    canvas:
        Rectangle:
            pos:self.center_x-5,0
            size: 10,self.height

    Label:
        font_size:70
        center_x:root.width/4
        top:root.top-50
        text:'0'


    Label:
        font_size:70
        center_x:root.width*3/4
        top:root.top-50
        text:'0'


    PongBall:
        id:Pong_ball
        center:self.parent.center

    PongPaddle:
        id:paddle_left
        x:root.x
        center_y:root.center_y

    PongPaddle:
        id:paddle_right
        x:root.width-self.width
        center_y:root.center_y


'''
