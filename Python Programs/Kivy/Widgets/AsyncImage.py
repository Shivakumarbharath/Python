from kivy.app import App
from kivy.uix.image import AsyncImage


class ImageApp(App):
    def build(self):
        img = AsyncImage(
            source='https://i.pinimg.com/236x/94/0d/9a/940d9a43fac3374d6b53e3cb6128d837--quill-peacock.jpg')

        return img


ImageApp().run()
