from tkinter import *

root = Tk()


def myClick(event):
    label = Label(root,
                  text="Clicked the Button at x={} y= {} and key ={}".format(str(event.x), str(event.y), event.keysym))
    label.pack()

    '''
    event.x=x -cordinate
    event.y=y-cordinate
    event.char= which char pressed
    event.keysym to get the sybol of the key to be used elsewhere
    
    
    '''


myButton = Button(root, text="click mee!")  # ,command=myClick,bg='blue')#creating a button
# myButton.bind(event,action)
'''
<Button-1> mouse normal click(event.x and y used for mouse )
<Button-2> mouse middle click
<Button-> mouse right click
<Enter> if mouse enters the widget
<Leave> if mouse leaves the widget
<FocusIn> To focus on the widget using the tab
<FocusOut> To tab away from the widget
<Return> Enter key works if tabbed (highlighted) 
<Key> any key on the keyboard after focused (event.char used)
more event formats at
https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
'''

myButton.bind("<Key>", myClick)
myButton.pack()

root.mainloop()
