from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class MyGrid(Widget):
    pass


class FloatApp(App):
    def build(self):
        return FloatLayout()


FloatApp().run()
