from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder


class Main(Screen):
    input1 = ObjectProperty()

    def btn(self):
        print(self.input1.text)
        self.passw = input('enter')


class Screen2(Screen):
    pass


class Manager(ScreenManager):
    pass


kv = Builder.load_file('Multiple.kv')


class MultipleApp(App):
    def build(self):
        return kv


MultipleApp().run()
