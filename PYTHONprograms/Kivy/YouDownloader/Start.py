from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty




class Option(Screen):

    def on_pre_enter(self, *args):
        Window.clearcolor = (0.15, 0.15, 1, 1)

class Video(Screen):
    def on_pre_enter(self, *args):
        Window.clearcolor=(1,1,1,1)



class Audio(Screen):

    url=ObjectProperty(None)
    rv=ObjectProperty(None)
    dat = []
    def on_pre_enter(self, *args):
        Window.clearcolor=(1,1,1,1)


        for l in ["label1", "label2", " label3"]:
            self.dat.append({'text':l,'color':(0,0,0,1)})
            self.ids.rv.data = self.dat
    def selected(self):
        print(self.rv.data)


class Manager(ScreenManager):
    pass


sm = ScreenManager()
kv = Builder.load_file('You.kv')

class YouApp(App):
    def build(self):
        Window.size = (360, 600)
        self.icon=r'icon.png'
        sm.add_widget(Option())
        sm.add_widget(Video())
        sm.add_widget(Audio())
        return sm


YouApp().run()
