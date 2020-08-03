from kivy.app import App
from kivy.lang import Builder
'''
The Builder class is in charge of loading and parsing all the Kivy
language. The load_file method allows us to specify a file containing
Kivy language rules that we want to include as part of the project.
'''
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('GeneralOptions.kv')
Builder.load_file('DrawingSpace.kv')
Builder.load_file('Statusbar.kv')
Builder.load_file('ToolBox.kv')


class ComicCreator(AnchorLayout):
    pass


class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()

if __name__=='__main__':
    ComicCreatorApp().run()