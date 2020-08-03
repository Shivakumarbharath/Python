from tkinter import *

root = Tk()

root.geometry('600x600')
# create a canvas widget

w = 400
h = 400
x = w // 2
y = h // 2

my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=30)

'''
#create a rectangle

#my_canvas.create_rectangle(x1,y1,x2,y2,)
#x1 y1 top left
#x2 y2 bottom right

my_canvas.create_rectangle(100,200,150,100,fill='blue')


#create a line inside the canvasr


#my_canvas.create_line(x1,y1,x2,y2,fill='colour')
my_canvas.create_line(0,0,200,200,)#my_canvas.create_line(0,200,200,0)
my_canvas.create_line(0,0,150,200)

#my_canvas.create_oval(x1,y1,x2,y2,)
#x1 y1 top left
#x2 y2 bottom right
'''
my_circle = my_canvas.create_oval(x, y, 100, 100)


def left(event):
    x = -10
    y = 0
    my_canvas.move(my_circle, x, y)


def up(event):
    x = 0
    y = -10
    my_canvas.move(my_circle, x, y)


def down(event):
    x = 0
    y = 10
    my_canvas.move(my_circle, x, y)


def right(event):
    x = 10
    y = 0
    my_canvas.move(my_circle, x, y)


# keyboard actions
root.bind("<Left>", left)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Right>", right)


# using letters
def press(event):
    x, y = 0, 0
    if event.char == 'a': x = -10
    if event.char == 'd': x = 10
    if event.char == 'w': y = -10
    if event.char == 's': y = 10

    my_canvas.move(my_circle, x, y)


root.bind("<Key>", press)

root.mainloop()
