from kivy.app import App
from kivy.uix.widget import Widget


class buttonpy(Widget):
    pass


class Buttons2App(App):
    def build(self):
        return buttonpy()

if __name__=='__main__':
    Buttons2App().run()

'''
<MyButton@Button>
    colour:.8,.9,0,1
    size:50,50
    font_size:15


<buttonpy>
    MyButton:
        pos: root.x, root.top - self.height
        text:"Hello"

    MyButton:
        pos: root.right - self.width, root.y
        text:"World"


Here my button is a customised class using the Buttin class this can be done by 
using the @ symbol
<ownName@className>

'''