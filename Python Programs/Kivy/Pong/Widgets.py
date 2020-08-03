from kivy.app import App

#All the widgets are in this Widget module
from kivy.uix.widget import Widget
#This is the basic window creation
class PongGame(Widget):#build of game is done in this class
    pass

class PongApp(App):#in this class the app is created in which pong game will run
    def build(self):
        return PongGame()


#to run the app
PongApp().run()


'''
To add a rectangle
You have to create a kv file written in kvland
The window is a sx cordinate system with 0,0 at the 
top left corner

The name of the kv file should be the name of the app
Example
PongApp(App)-so the kv file
Pong.kv



<PongGame>
    canvas:#in the canvas all shapes can be added 
        Rectangle:
            pos:self.center_x-5,0#x,y
            size: 10,self.height#width,height
            
            
            
            
    Label:#for labels
    font_size:70
    center_x:root.width/4#x axis
    top:root.top-50#y axis from top
    text:'0'


    Label:
        font_size:70
        center_x:root.width*3/4
        top:root.top-50
        text:'0'



'''