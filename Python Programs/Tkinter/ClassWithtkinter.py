from tkinter import *

root = Tk()


class Hello:
    def __init__(self, rootwindow):
        myframe = Frame(rootwindow, bg='red')
        myframe.pack()

        self.button = Button(rootwindow, text="Click", command=self.click)
        self.button.pack(pady=10)

    def click(self):
        print('You clicked')


o = Hello(root)

root.mainloop()
