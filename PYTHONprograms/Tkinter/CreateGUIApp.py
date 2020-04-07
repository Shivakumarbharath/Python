'''

In tkinter Everything is a widget
like button widgets text widgets etc etc

THe first thing we create is the root widget that is a window
the second is to display it
'''



from tkinter import *
import time
window=Tk()
#this should be first before anything
#this will be used in every widget we make
# basically it creates a window

#To resize the window
window.geometry('600x300')#this is the size of the window (width x length)

#provide a title to the window

window.title("Learn Tkinter")

#To print on the window
#in any funtion we have to provide the widow variable first
label1=Label(window,text='Welcome To the New Chapter',fg= 'blue',bg='yellow',relief='solid',font=('ariel',13,'bold')).pack()
#in this way the basic label is created

#positioning the label
#pack basically takes at the top of the window
#label=Label(window,text='Welcome To the New Chapter',fg= 'blue',bg='yellow',relief='solid',font=('ariel',13,'bold')).pack()
label2=Label(window,text='Postition hah',fg= 'black',bg='white',font=('ariel',10)).place(x=450,y=200)



labe2=Label(window,text='Postition ',fg= 'black',bg='white',font=('ariel',10)).place(x=450,y=200)

'''
Event loop
When we have a gui we have a programm running that is looping always constantly
and thats how it figures out whats going on
as its looping u might move your mouse


And when the programm ends the loop ends


'''
window.mainloop()