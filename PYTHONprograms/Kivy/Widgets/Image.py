from kivy.app import App
from kivy.uix.image import Image

class ImageApp(App):
    def build(self):
        img=Image(source='E:\Bharath\Python\PYTHONprograms\Kivy\LoginForm\loginpage.png')


        return img

ImageApp().run()