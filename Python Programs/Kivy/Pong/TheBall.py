from kivy.app import App

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty  # similar to datatypes
from kivy.vector import Vector  # to get the vector postion
from kivy.clock import Clock
import random


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

    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(random.randint(0,360))

    def update(self, dt):
        self.ball.move()


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


# to run the app
PongApp().run()

'''
<PongBall>
    size:50,50#width ,height
    canvas:
        Ellipse:
            pos:self.pos
            size:self.size#take the above size



<PongGame>
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


    PongBall:#include the ball widget into the game
        center:self.parent.center



'''
