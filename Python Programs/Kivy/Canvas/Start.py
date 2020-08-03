from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout


class DrawIt(RelativeLayout):
    pass


class DrawingApp(App):
    def build(self):
        return DrawIt()


DrawingApp().run()
