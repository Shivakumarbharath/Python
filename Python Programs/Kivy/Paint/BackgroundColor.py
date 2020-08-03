from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window  # To customize the window

Window.clearcolor = (0, 1, 1,1)  # rgba format to change the colour of the window


class PaintWindow(Widget):
    pass


class PaintApp(App):
    def build(self):
        return


PaintApp().run()
