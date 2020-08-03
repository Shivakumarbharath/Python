from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class floatlayoutApp(App):
    def build(self):
        return FloatLayout()

if __name__=="__main__":
    floatlayoutApp().run()


'''
to customise the button class ,remember the colon ":"
<Button>:
    colour:.8,.9,0,1
    font_size:15
    size_hint:.5,.5


<FloatLayout>
    Button:
        text:'Shivakumar'
        pos_hint: {'x': 0, 'top': 1}

    Button:
        text:'Bharath'
        pos_hint: {'right': 1, 'y': 0}


In the floatlayout.kv code file, we use two new properties, size_hint and
pos_hint, which work with the proportional coordinates with values ranging from
0 to 1;

 (0, 0) is the bottom-left corner and (1, 1) the top-right corner
 
 
 size hint is the percentage of the window
 50% of x axis and 50%of y axis
 
 
 . The top and right properties respectively
reference the top and right edges of the Button, so it makes the positioning simpler.  


The available pos_hint keys (x, center_x, right, y, center_y, and top) 




For example, instead of pos: root.x, root.top - self.
height, we would have used the following code:
 x: 0
 top: root.height
Notice that these properties always specify fixed values (pixels) and not
proportional ones


'''