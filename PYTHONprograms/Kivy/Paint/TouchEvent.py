from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window  # To customize the window
from kivy.graphics import Ellipse,Color
Window.clearcolor = (0, 0, 0,0)  # rgba format to change the colour of the window


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        self.canvas.add(Color(rgb=(1,0,0)))
        self.canvas.add(Ellipse(pos=[touch.x-15,touch.y-15],size=(30,30)))



class PaintApp(App):
    def build(self):
        return PaintWindow()


PaintApp().run()
