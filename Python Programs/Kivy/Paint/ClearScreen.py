from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window  # To customize the window
from kivy.graphics import Ellipse, Color, Line
import random

Window.clearcolor = (1, 1, 1, 0)  # rgba format to change the colour of the window


# Root Window=Paint Window +Button
class PaintWindow(Widget):
    def on_touch_down(self, touch):
        # to make colour random
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)

        self.canvas.add(Color(rgb=(colorR / 255.0, colorG / 255.0, colorB / 255.0)))
        # self.canvas.add(Ellipse(pos=[touch.x-15,touch.y-15],size=(30,30)))
        # To note the points where the mmouse has moved we use touch dictionary
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

        '''
        Algorithim for making a brush
        1.Import the line graphics
        2.create a touch dictionary->store the initial point in it
        3. when the mouse is draged store that points
        4.store it inside the canvas

        '''

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        # touch.ud['line'].points += [touch.x, touch.y]
        # when released the line is formed if the method on touch move is not used
        pass


class PaintApp(App):
    def build(self):
        # create a window
        rootWindow = Widget()
        self.paint = PaintWindow()
        btn = Button(text="Clear", on_press=self.clear)
        rootWindow.add_widget(btn)
        rootWindow.add_widget(self.paint)
        return rootWindow

    def clear(self, obj):
        self.paint.canvas.clear()


PaintApp().run()
