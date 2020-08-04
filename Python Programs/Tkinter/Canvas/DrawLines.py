from tkinter import *

root = Tk()

root.geometry('400x400')
# create a canvas widget
my_canvas = Canvas(root, width=200, height=200, bg='white')
my_canvas.pack()

# create a rectangle

# my_canvas.create_rectangle(x1,y1,x2,y2,)
# x1 y1 top left
# x2 y2 bottom right

my_canvas.create_rectangle(100, 200, 150, 100, fill='blue')

# create a line inside the canvasr


# my_canvas.create_line(x1,y1,x2,y2,fill='colour')
my_canvas.create_line(0, 0, 200, 200, )  # my_canvas.create_line(0,200,200,0)
my_canvas.create_line(0, 0, 150, 200)

# my_canvas.create_oval(x1,y1,x2,y2,)
# x1 y1 top left
# x2 y2 bottom right

my_canvas.create_oval(100, 200, 150, 100, fill='yellow')

root.mainloop()
