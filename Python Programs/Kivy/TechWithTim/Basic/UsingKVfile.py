from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)

    def Pressed(self):
        # to get the text entered
        name = self.firstname.text
        last = self.lastname.text
        email = self.email.text

        print(name, last, email)

        # to clear the text
        self.firstname.text = ''
        self.lastname.text = ''
        self.email.text = ''

        print("presed")


class My2App(App):
    def build(self):
        return MyGrid()


My2App().run()

'''
<MyGrid>

    firstname:firstname
    lastname:lastname
    email:email
    GridLayout:
        cols:1
        size:root.width,root.height


        GridLayout:#grid inside a grid layout
            cols:2

            Label:
                text:'First Name'
            TextInput:
                id:firstname
                multiline:False

            Label:
                text:'Last Name'
            TextInput:
                id:lastname
                multiline:False

            Label:
                text:'Email'
            TextInput:
                id:email
                multiline:False


        Button:
            text:'Submit'
            on_press:root

'''
