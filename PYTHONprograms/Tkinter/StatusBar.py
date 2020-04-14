#WE will use the imag viewing app to make a status bar

from tkinter import *
from PIL import Image,ImageTk


#To View the status bar go to line number 29

root= Tk()

root.title('Images ')

#create the buttons and image

extBtn=Button(root,text='Exit',command=root.quit)
forward_Btn=Button(root,text='>>',command=lambda:forward(2))
backward_Btn=Button(root,text='<<',state='disabled',command=lambda: backward(0))



my_img1=ImageTk.PhotoImage(Image.open('Viewer\Destination_1.jpg'))
my_img2=ImageTk.PhotoImage(Image.open('Viewer\Destination_2.jpg'))
my_img3=ImageTk.PhotoImage(Image.open('Viewer\Destination_3.jpg'))
my_img4=ImageTk.PhotoImage(Image.open('Viewer\Destination_4.jpg'))

#list of all the images
img_lst=[my_img1,my_img2,my_img3,my_img4]

#creating A status bar

status=Label(root,text="Image 1 of " + str(len(img_lst)),bd=1,relief=SUNKEN,anchor=W)

'''
bd- for the border
To look sunkun down a lttle bit so we use 

relief-SUNKEN
There are 4 options for relief
1.SUNKEN
2.RIDGE
3.GROOVE
4.RASIED

anchor - to place it in the sunken place that is east or west

To update it put it in the function

Go to line number 56
'''

#place the created things in window

lab=Label(root,image=my_img1)
lab.grid(row=0,column=0,columnspan=3)


extBtn.grid(row=1,column=1,pady=10)#pady is togive some space
forward_Btn.grid(row=1,column=2)
backward_Btn.grid(row=1,column=0)

status.grid(row=2,column=0,columnspan=3,sticky=W+E)
# Stick the Sunken part all over West to East

#


#functions that works when the buttons are pressed
def forward(num):
    # since the variables in one function cannot be used in other function we make the variables global
    global lab
    global forward_Btn
    global backward_Btn

    # to remove the image first
    lab.grid_forget()
    lab = Label(root, image=img_lst[num - 1])
    #if the button is pressed again to perform the same function using recursion
    forward_Btn=Button(root,text=">>",command=lambda:forward(num+1))
    backward_Btn = Button(root, text="<<", command=lambda: backward(num - 1))

    #To avoid Index Range Error

    if num == 4:
        forward_Btn=Button(root,text='>>',state=DISABLED)
        forward_Btn.grid(row=1,column=2)

    #placing theButtons on to the window

    lab.grid(row=0, column=0, columnspan=3)
    forward_Btn.grid(row=1,column=2)
    backward_Btn.grid(row=1, column=0)

    # update the status bar
    status = Label(root, text="Image "+str(num)+" of " + str(len(img_lst)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    return

def backward(num):
    global lab
    global forward_Btn
    global backward_Btn
    lab.grid_forget()
    lab = Label(root, image=img_lst[num-1])

    forward_Btn = Button(root, text=">>", command=lambda: forward(num+1))
    backward_Btn = Button(root, text="<<", command=lambda: backward(num - 1))

    if num == 1:
        backward_Btn = Button(root, text='<<', state=DISABLED)
        backward_Btn.grid(row=1, column=0)

    lab.grid(row=0, column=0, columnspan=3)
    forward_Btn.grid(row=1,column=2)
    backward_Btn.grid(row=1, column=0)

    #update the status bar
    status = Label(root, text="Image " + str(num) + " of " + str(len(img_lst)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    return


#run the loop
root.mainloop()
