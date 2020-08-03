'''
Four Steps
1.Create an app
2.Create a game 
3.Build the game
4.Run the app

'''
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


'''