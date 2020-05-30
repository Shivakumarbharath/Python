from tkinter import *

root =Tk()

root.geometry('600x600')
#create a canvas widget

w=400
h=400
x=50
y=50

my_canvas=Canvas(root,width=w,height=h,bg='white')
my_canvas.pack(pady=30)

my_circle=my_canvas.create_oval(x,y,100,100)

def press(e):
    global my_circle

    #since the move method takes amount of move
    #we cannot use e.x and e.y as it becomes the amount of move and gets disapperared
    #so better to use this method
    my_canvas.delete(my_circle)
    my_circle = my_canvas.create_oval(e.x, e.y, e.x+50, e.y+50)



my_canvas.bind("<B1-Motion>",press)


root.mainloop()