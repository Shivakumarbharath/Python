from tkinter import *

root=Tk()
root.geometry("400x400")
#panels
panel_1=PanedWindow(bd=4,relief=RAISED,bg='red')#normally not visible
panel_1.pack(fill =BOTH,expand=1)

left_label1=Label(panel_1,text="panel 1")
panel_1.add(left_label1)

#panel in panel
panel_2=PanedWindow(panel_1,bd=4,relief=RAISED,bg='yellow',orient=VERTICAL)#normally not visible
panel_1.add(panel_2)

left_label2=Label(panel_1,text="right panel")
panel_1.add(left_label2)

top=Label(panel_2,text="top panel")
panel_2.add(top)

bottom=Label(panel_2,text='Bottom Pannel')
panel_2.add(bottom)

mid=Label(panel_2,text="Mid")
panel_2.add(mid)



root.mainloop()