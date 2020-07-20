from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.rows=2
        #to make it as two different grids we have make a grid inside this
        self.inside=GridLayout()
        self.inside.cols=2
        self.inside.add_widget(Label(text="First Name :"))#to add a widget
        self.first_name=TextInput(multiline=False)#textinput by the user
        self.inside.add_widget(self.first_name)#to add the text input

        self.inside.add_widget(Label(text="Last Name :"))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="Email :"))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        #add this grid into the window
        self.add_widget(self.inside)

        #add a button
        self.submit=Button(text="Submit",font_size=15)
        self.add_widget(self.submit)#add it on the screen

        #provide functionality
        self.submit.bind(on_press=self.Pressed)




    def Pressed(self,instance):
        #to get the text entered
        name=self.first_name.text
        last=self.last_name.text
        email=self.email.text

        print(name,last,email)

        #to clear the text
        self.first_name.text=''
        self.last_name.text=''
        self.email.text=''

        print("presed")

class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()