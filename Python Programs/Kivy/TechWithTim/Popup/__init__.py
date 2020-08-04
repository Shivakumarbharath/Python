from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder

Builder.load_file('p.kv')


class Widg(Widget):
    def Btn(self):
        show_popup()


class P(FloatLayout):
    pass


class MyPopApp(App):
    def build(self):
        return Widg()


def show_popup():
    show = P()
    pop = Popup(title="My PopUP", content=show, size_hint=(None, None), size=(400, 400), )
    pop.open()


MyPopApp().run()
