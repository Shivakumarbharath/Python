from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout


class Images(RelativeLayout):
    pass


class ImageApp(App):
    def build(self):
        return Images()


ImageApp().run()
