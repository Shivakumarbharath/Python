from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=2#number of columns

        self.add_widget(Label(text="First Name :"))#to add a widget
        self.first_name=TextInput(multiline=False)#textinput by the user
        self.add_widget(self.first_name)#to add the text input

        self.add_widget(Label(text="Last Name :"))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.add_widget(Label(text="Email :"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()