from kivy.app import App  # creation of an app
from kivy.uix.label import Label


class HelloApp(App):  # The App class is the starting point of any Kivy #application.

    def build(self):
        return Label(text='Hello World')


if __name__ == "__main__":
    HelloApp().run()
