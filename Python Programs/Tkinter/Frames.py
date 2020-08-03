from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Use your Frames')
'''
Frames is just like border or a box
We can have a label
Its used to keep things organised in your apps
We might have different sections we want to sort of put together visually
And a frame is a good way to do that.
Its jus a widget just as other widgets
 

'''
# Create the frame
frame = LabelFrame(root, text="This is my frame... ", padx=5, pady=30)  # inside of the frame padding

# place it on the window
frame.pack(padx=50, pady=10)  # outside of the frame padding

# button in the frame
b = Button(frame, text="Don't Touch", command=root.quit)

b2 = Button(frame, text="Neither Here", command=root.quit)
b.grid(row=0, column=0)

b2.grid(row=1, column=1)

root.mainloop()
