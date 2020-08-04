from kivy.app import App
from kivy.uix.widget import Widget


class mywidgets(Widget):
    pass


class WidgetApp(App):
    def build(self):
        return mywidgets()


if __name__ == '__main__':
    WidgetApp().run()

'''
<mywidgets>
    Button:
        text:'HEllO'
        pos:root.center_x,100
        size:50,50
        font_size:15
        colour:.8,.9,0,1

    Button:
        text:'Brother'
        pos:100,50
        size:50,50
        font_size:15
        colour:.8,.9,0,1


Notice that the coordinate (0, 0) is at the bottom-left
corner, that is, the Cartesian origin

(the color is in RGBA
format that stands for red, green, blue, and alpha/transparency

'''
