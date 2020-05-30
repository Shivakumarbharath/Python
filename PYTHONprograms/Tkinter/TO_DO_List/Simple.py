from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry('400x400+100+150')
root.title("My-to-List")
root.resizable(0,0)
class Create:
    tasks_dict={}
    def __init__(self,master):
        #Create a frame and pack
        self.baseFrame=Frame(master,bg='white')
        self.baseFrame.pack(fill=BOTH,expand=1)

        #Create a scroll bar object
        self.my_scrollbar = Scrollbar(self.baseFrame, orient=VERTICAL)


        #Create a canvas object and pack it in base frame and also provide the dcroll command
        self.canvas=Canvas(self.baseFrame,width=200,height=300,bg='yellow',yscrollcommand=self.my_scrollbar.set)
        self.canvas.place(relx=0.27,rely=0.12)



        #create a container frame to add the tasks
        self.containerFrame=Frame(self.canvas,bg='red')#,yscrollcommand=self.my_scrollbar.set)
        self.window=self.canvas.create_window(0,0,window=self.containerFrame,anchor = NW)

        #provide the command to the dcroll bar (confiure and place)
        self.my_scrollbar.config(command=self.canvas.yview)
        self.my_scrollbar.place(relx=0.78,rely=0.12,height=304)

        #Bind the functionality of scroll bar to container frame
        self.containerFrame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )




        #add buttons
        #to add the task entry

        self.addButton=Button(self.baseFrame,text="Add task",command=self.Ask_task)#,command=lambda :self.Add_task("jlfksdfj"))
        self.addButton.place(relx=0.3,rely=0.9)

        #save changes of the task
        self.save_buttonn=Button(self.baseFrame,text="Save changes",command=self.Save)
        self.save_buttonn.place(relx=0.5,rely=0.9)



        #Database connection
        self.database=sqlite3.connect("DO_Not_Delete.db")
        self.c=self.database.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS general(
        tasks TEXT,
        status INTEGER
        )""")

        self.database.commit()
        self.database.close()

        #To get from the database if previously stored
        self.Retrive_from_database()

        #mouse wheel binding
        self.canvas.bind('<Enter>', self._bound_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbound_to_mousewheel)


    #The 3 functions are used to bound the mouse wheel to the scroll bar
    def _bound_to_mousewheel(self, event):#to bound only when the mouse is inside the canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):#to unbind the mouse wheel when outside the canvas
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):#funtion while binding
        self.canvas.yview_scroll(int(-1 * (event.delta / 100)), "units")
        #the first parameter is for controlling the speed
        #can bse changed by changing the number 100



    # to add the task to the container frame and to the memory
    def Add_task(self,text):

        self.task=IntVar()

        c = Checkbutton(self.containerFrame, text=text,variable=self.task, onvalue=1, offvalue=0)
        c.pack(padx=10,pady=10,anchor=W)
        c.deselect()
        self.tasks_dict[text]=(self.task,self.task.get())
        self.Add_to_database(text,self.task.get())
        self.ask.destroy()
        #except:
         #   k=messagebox.showerror("Excessive Add Eask Windows","Cancel All the add task windows and try again")

    #To get the task from the user and to add to the dictionary
    def Ask_task(self):
        self.ask=Toplevel()
        self.ask.geometry('200x100+150+200')
        self.task_Entry=Entry(self.ask,width=28)
        self.task_Entry.place(relx=0.05,rely=0.4)
        Label(self.ask,text="Your Task :",font=('ariel',12,'bold')).place(relx=0.05,rely=0.15)


        self.Ad_button=Button(self.ask,text="Add",command=lambda :self.Add_task(self.task_Entry.get()))
        self.Ad_button.place(relx=0.1,rely=0.6)


    #to saves the changes in the database
    def Save(self):
        for e in self.tasks_dict:
            self.tasks_dict[e]=(self.tasks_dict[e][0],self.tasks_dict[e][0].get())

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        for e in self.tasks_dict:#to change in the dictionary and in database
            self.tasks_dict[e]=(self.tasks_dict[e][0],self.tasks_dict[e][0].get())
            self.c.execute("UPDATE general  SET status={} WHERE  tasks='{}'".format(self.tasks_dict[e][0].get(),e))

        self.details=self.c.execute("SELECT oid,* FROM general")
        print(self.details.fetchall(),'line93')
        self.database.commit()
        self.database.close()

        print(self.tasks_dict)

    #To add the new entry to the database
    def Add_to_database(self,entries,status_of_entry):
        self.database=sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.c.execute("""INSERT INTO general
        VALUES ('{}', {})""".format(entries,status_of_entry))

        self.database.commit()
        self.database.close()

    #To retrive from the database and display in the form of comboboxes
    def Retrive_from_database(self):

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.details = self.c.execute("SELECT oid,* FROM general").fetchall()
        temp_lst=[]
        widgetlist=[]

        if len(self.details)>0:

            for e in self.details:

                #variavle initialisation
                variable=IntVar()
                #since diferent variables are needed for each combobox
                #add and use the last element in the list
                temp_lst.append(variable)
                widgetlist.append(Checkbutton(self.containerFrame,variable=temp_lst[-1], text=e[1], onvalue=1, offvalue=0))
                widgetlist[-1].pack(padx=10, pady=10, anchor=W)

                #if the task is already done and stored in the database
                #to check the combobox
                if e[2]==1:
                    widgetlist[-1].select()
                else:
                    widgetlist[-1].deselect()


                #set the result from the database to the variable in the list
                temp_lst[-1].set(e[2])
                #save it to the dictionary so that all the changes is done from the dictionary
                self.tasks_dict[e[1]] = (temp_lst[-1], e[2])


        self.database.commit()
        self.database.close()


'''
class Create2:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.canvas = Canvas(frame, bg='pink')
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=True)

        self.mailbox_frame = Frame(self.canvas, bg='purple')

        self.canvas_frame = self.canvas.create_window((0, 0),
                                                      window=self.mailbox_frame, anchor=NW)
        # self.mailbox_frame.pack(side = LEFT, fill = BOTH, expand = True)

        mail_scroll = Scrollbar(self.canvas, orient="vertical",
                                command=self.canvas.yview)
        mail_scroll.pack(side=RIGHT, fill=Y)

        self.canvas.config(yscrollcommand=mail_scroll.set)

        self.entry=Entry(self.mailbox_frame)
        self.entry.pack()

        #self.mailbox_frame.bind("<Configure>", self.OnFrameConfigure)
        #self.canvas.bind('<Configure>', self.FrameWidth)
'''

obj=Create(root)
root.mainloop()