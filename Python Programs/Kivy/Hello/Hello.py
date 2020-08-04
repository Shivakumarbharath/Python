from kivy.app import App  # creation of an app
from kivy.uix.label import Label

'''
 Kivy
offers its own language to separate the logic from the presentation. 

The initial part of the App's subclass name has to coincide with
the name of the Kivy file. For example, if the definition of the
class is class FooApp(App), then the name of the file must
be foo.kv and it must be in the same directory of the main file
(the one that executes the App's run() method).


'''


class Hello2App(App):  # The App class is the starting point of any Kivy #application.

    def build(self):
        return Label()


if __name__ == "__main__":
    Hello2App().run()
'''
# File name: hello2.kv

<Label>
    text:'Hello World'
    
    
    The <Label>: rule (line 26) indicates that we are going to modify the Label class
by setting 'Hello World!' in the text property (line 27).

'''
