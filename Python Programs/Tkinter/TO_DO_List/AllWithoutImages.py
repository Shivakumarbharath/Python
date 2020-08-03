from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

import sqlite3

root = Tk()


# root.geometry('500x500+100+100')
# root.title("Things To DO")
# root.iconbitmap("icon.ico")
# root.resizable(0,0)

class Create_Category:
    tasks_dict = {}
    widgetlist = []

    def __init__(self, master, catogory_name):
        self.catogory_name = catogory_name
        # Create a frame and pack
        self.baseFrame = Frame(master, bg='white')
        self.baseFrame.pack(fill=BOTH, expand=1)

        # Create a scroll bar object
        self.my_scrollbar = Scrollbar(self.baseFrame, orient=VERTICAL)

        # Create a canvas object and pack it in base frame and also provide the dcroll command
        self.canvas = Canvas(self.baseFrame, width=200, height=300, bg='white', yscrollcommand=self.my_scrollbar.set,
                             borderwidth=0)
        self.canvas.place(relx=0.27, rely=0.12)

        # create a container frame to add the tasks
        self.containerFrame = Frame(self.canvas, bg='white', borderwidth=0)  # ,yscrollcommand=self.my_scrollbar.set)
        self.window = self.canvas.create_window(0, 0, window=self.containerFrame, anchor=NW)

        # provide the command to the dcroll bar (confiure and place)
        self.my_scrollbar.config(command=self.canvas.yview)
        self.my_scrollbar.place(relx=0.677, rely=0.12, height=304)

        # Bind the functionality of scroll bar to container frame
        self.containerFrame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        '''
        # images
        # file names
        mob_file = 'feather.jpg'
        tick_file = 'logo.jpg'
        # open image
        mob_img = Image.open(mob_file)
        tick_img = Image.open(tick_file)
        # resize images
        mob_img_resize = mob_img.resize((90, 300))
        tick_img_resize = tick_img.resize((90, 90))
        # connecting the images to tkinter
        self.baseFrame.mob_image = ImageTk.PhotoImage(mob_img_resize)
        self.baseFrame.tick_image = ImageTk.PhotoImage(tick_img_resize)
        # label images
        lab_mob = Label(self.baseFrame, image=self.baseFrame.mob_image, bg='white')
        lab_tick = Label(self.baseFrame, image=self.baseFrame.tick_image, bg='white')
        # place images
        lab_mob.place(relx=0.75, rely=0.1)
        lab_tick.place(relx=0.05, rely=0.0)
        '''
        self.catogory_label = Label(self.baseFrame, text=self.catogory_name.title(),
                                    font=('Helvatica', 15, 'bold italic'), bg='White', fg='blue')
        self.catogory_label.place(relx=0.35, rely=0.045)

        # add buttons
        # to add the task entry

        self.addButton = Button(self.baseFrame, text="Add task",
                                command=self.Ask_task, relief=GROOVE,
                                fg='blue')  # ,command=lambda :self.Add_task("jlfksdfj"))
        self.addButton.place(relx=0.2, rely=0.8)

        # save changes of the task
        self.save_buttonn = Button(self.baseFrame, text="Save changes", command=self.Save, relief=GROOVE, fg='green')
        self.save_buttonn.place(relx=0.4, rely=0.8)

        # to delete any entries
        self.del_entrry = Button(self.baseFrame, text="Delete Task", command=self.Delete_window, relief=GROOVE,
                                 fg='red')
        self.del_entrry.place(relx=0.65, rely=0.8)

        # Database connection
        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS {}(
        tasks TEXT,
        status INTEGER
        )""".format(self.catogory_name))

        self.database.commit()
        self.database.close()

        # To get from the database if previously stored
        self.Retrive_from_database()
        print(self.tasks_dict, '79')

        # mouse wheel binding
        self.canvas.bind('<Enter>', self._bound_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbound_to_mousewheel)

    # The 3 functions are used to bound the mouse wheel to the scroll bar
    def _bound_to_mousewheel(self, event):  # to bound only when the mouse is inside the canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):  # to unbind the mouse wheel when outside the canvas
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):  # funtion while binding
        self.canvas.yview_scroll(int(-1 * (event.delta / 100)), "units")
        # the first parameter is for controlling the speed
        # can bse changed by changing the number 100
        ''' Stack overflow says
        Note that self.canvas.bind_all is a bit misleading -- you more correctly should call root.bind_all but 
        I don't know what or how you define your root window. Regardless, the two calls are synonymous.

        Platform differences:

        On Windows, you bind to <MouseWheel> and you need to divide eve
        nt.delta by 120 (or some other factor depending on how fast you want the scroll)
        '''

    # to add the task to the container frame and to the memory
    def Add_task(self, text):

        self.task = IntVar()

        c = Checkbutton(self.containerFrame, text=text.title(), variable=self.task, onvalue=1, offvalue=0, bg='white')
        c.pack(padx=10, pady=10, anchor=W)
        c.deselect()
        self.widgetlist.append(c)
        self.tasks_dict[text] = (self.task, self.task.get())
        self.Add_to_database(text, self.task.get())
        self.ask.destroy()
        # except:
        #   k=messagebox.showerror("Excessive Add Eask Windows","Cancel All the add task windows and try again")

    # To get the task from the user and to add to the dictionary
    def Ask_task(self):
        self.ask = Toplevel()
        self.ask.geometry('200x100+150+200')
        self.task_Entry = Entry(self.ask, width=28)
        self.task_Entry.place(relx=0.05, rely=0.4)
        Label(self.ask, text="Your Task :", font=('ariel', 12, 'bold')).place(relx=0.05, rely=0.15)

        self.Ad_button = Button(self.ask, text="Add", command=lambda: self.Add_task(self.task_Entry.get()))
        self.Ad_button.place(relx=0.1, rely=0.6)

    # to saves the changes in the database
    def Save(self):

        for e in self.tasks_dict:
            self.tasks_dict[e] = (self.tasks_dict[e][0], self.tasks_dict[e][0].get())

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        for e in self.tasks_dict:  # to change in the dictionary and in database
            self.tasks_dict[e] = (self.tasks_dict[e][0], self.tasks_dict[e][0].get())
            self.c.execute(
                "UPDATE {}  SET status={} WHERE  tasks='{}'".format(self.catogory_name, self.tasks_dict[e][0].get(), e))

        self.details = self.c.execute("SELECT oid,* FROM {}".format(self.catogory_name))
        # print(self.details.fetchall(), 'line93')
        self.database.commit()
        self.database.close()

        k = messagebox.showinfo('Save', 'Changes Saved to DataBase')

    # To add the new entry to the database
    def Add_to_database(self, entries, status_of_entry):
        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.c.execute("""INSERT INTO {}
        VALUES ('{}', {})""".format(self.catogory_name, entries, status_of_entry))

        self.database.commit()
        self.database.close()

    # To retrive from the database and display in the form of comboboxes
    def Retrive_from_database(self):

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.details = self.c.execute("SELECT oid,* FROM {}".format(self.catogory_name)).fetchall()
        temp_lst = []
        self.widgetlist = []

        if len(self.details) > 0:

            for e in self.details:

                # variavle initialisation
                variable = IntVar()
                # since diferent variables are needed for each combobox
                # add and use the last element in the list
                temp_lst.append(variable)
                self.widgetlist.append(
                    Checkbutton(self.containerFrame, variable=temp_lst[-1], text=e[1].title(), onvalue=1, offvalue=0,
                                bg='white'))
                self.widgetlist[-1].pack(padx=10, pady=10, anchor=W)

                # if the task is already done and stored in the database
                # to check the combobox
                if e[2] == 1:
                    self.widgetlist[-1].select()
                else:
                    self.widgetlist[-1].deselect()

                # set the result from the database to the variable in the list
                temp_lst[-1].set(e[2])
                # save it to the dictionary so that all the changes is done from the dictionary
                self.tasks_dict[e[1]] = (temp_lst[-1], e[2])

        self.database.commit()
        self.database.close()

    def Delete_window(self):
        self.del_wind = Toplevel()
        self.del_wind.title("Select Entry to Delete")
        self.del_wind.geometry("300x250+150+150")
        self.del_wind.resizable(0, 0)
        self.list_frame = Frame(self.del_wind)
        self.delete_button = Button(self.del_wind, text="Delete",
                                    command=lambda: self.Delete_task(self.del_list.get(ANCHOR)))
        my_scrollbar = Scrollbar(self.list_frame, orient=VERTICAL)

        self.del_list = Listbox(self.list_frame, bd=3, width=40, yscrollcommand=my_scrollbar.set)
        my_scrollbar.config(command=self.del_list.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        self.list_frame.place(x=0, y=0)  # fill=BOTH,expand=1)
        self.del_list.pack(padx=15, pady=15)
        self.delete_button.place(relx=0.4, rely=0.8)

        for i, e in enumerate(self.tasks_dict):
            self.del_list.insert(i, e)

    def Delete_task(self, entry):

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.c.execute("DELETE FROM {} WHERE tasks='{}'".format(self.catogory_name, entry))

        self.database.commit()
        self.database.close()

        for e in self.widgetlist:
            e.destroy()

        self.tasks_dict = {}
        self.Retrive_from_database()

        self.del_wind.destroy()


class Menu_Class:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x500+100+100')
        self.root.title("Things To DO")
        self.root.iconbitmap("icon.ico")
        self.root.resizable(0, 0)

        self.main_menu = Menu(self.root)
        self.root.config(menu=self.main_menu)

        self.options = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Menu", menu=self.options)

        # self.options.add_command(label="Home", command=self.Home)
        self.options.add_separator()

        self.options.add_command(label="New", command=self.New)
        self.options.add_separator()

        self.options.add_command(label="Delete", command=self.Del_menu)
        self.options.add_separator()

        self.options.add_command(label="Change Name", command=self.Profile_name)
        self.options.add_separator()

        self.options.add_command(label="Exit", command=self.root.quit)

        # self.Home()
        self.file = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Categories", menu=self.file)
        self.Retrive_catagories()

    '''
    def Home(self):

        self.Del_children()

        self.IMAGE_PATH = 'background.jpg'
        WIDTH, HEIGTH = 500, 500

        self.canvas_home = Canvas(self.root, width=WIDTH, height=HEIGTH)
        self.canvas_home.pack()

        img = ImageTk.PhotoImage(Image.open(self.IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        self.canvas_home.background = img  # Keep a reference in case this code is put in a function.
        bg = self.canvas_home.create_image(0, 0, anchor=NW, image=img)

        qLab=Label(self.canvas_home,text='Conquer yourself and the\nwhole universe is yours...'.title(),bg='#f2f2f2',font=('helvatica',8,'italic'))
        qLab.place(relx=0.05,rely=0.9)


        self.Profile()
    '''

    # self.home_frame = Frame(self.root, bg='yellow')
    # self.home_frame.pack(fill=BOTH,expand=1)

    def Retrive_catagories(self):
        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()
        self.details = []
        try:
            self.details = self.c.execute("SELECT * FROM frames").fetchall()
        except:
            self.c.execute("""CREATE TABLE IF NOT EXISTS frames(
                        tasks TEXT 
                        )""")

        self.database.commit()
        self.database.close()

        for e in self.details:
            var = self.file.add_command(label=e[0], command=lambda k=e[0]: self.Call_category(k))

        print(self.details, '314')

    def Del_children(self):
        if self.root.winfo_exists() == 1:
            for e in self.root.winfo_children()[1:]:
                e.destroy()

    def Call_category(self, name):
        print(self.root.winfo_children(), '325')
        self.Del_children()

        Create_Category(self.root, name)
        print(self.root.winfo_children(), '325')

    def Create_Category_menu(self, name):
        # Hide_all_frames()

        # self.frame = Frame(self.root, bg='blue')

        Create_Category(self.root, name)

    def Newframe(self, name):
        self.new_create.destroy()

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.c.execute("""INSERT INTO frames
                        VALUES ('{}')""".format(name))

        self.database.commit()
        self.database.close()
        k = (name,)
        self.details.append(k)
        self.file.add_command(label=name, command=lambda: self.Call_category(name))
        self.Call_category(name)

    def New(self):

        self.new_create = Toplevel()
        self.new_create.config(bg="white")
        self.new_create.title("Create")
        self.new_create.geometry("250x100+250+250")
        self.new_create.resizable(0, 0)

        Label(self.new_create, text="Create category By Name:", fg='Orange', bg='white',
              font=('ariel', 12, 'bold')).place(relx=0.08, rely=0.17)
        name_of_category = Entry(self.new_create, width=33, bd=3)
        name_of_category.place(relx=0.10, rely=0.42)

        add_button = Button(self.new_create, text="Create", relief=GROOVE,
                            command=lambda: self.Newframe(name_of_category.get().replace(' ', '_')))
        add_button.place(relx=0.45, rely=0.67)

    def Del_menu(self):

        self.del_wind = Toplevel()
        self.del_wind.title("Select Category to Delete")
        self.del_wind.geometry("300x250+150+150")
        self.del_wind.resizable(0, 0)
        self.list_frame = Frame(self.del_wind)
        self.delete_button = Button(self.del_wind, text="Delete",
                                    command=lambda: self.Delete_task(self.del_list.get(ANCHOR)))
        my_scrollbar = Scrollbar(self.list_frame, orient=VERTICAL)

        self.del_list = Listbox(self.list_frame, bd=3, width=40, yscrollcommand=my_scrollbar.set)
        my_scrollbar.config(command=self.del_list.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        self.list_frame.place(x=0, y=0)  # fill=BOTH,expand=1)
        self.del_list.pack(padx=15, pady=15)
        self.delete_button.place(relx=0.4, rely=0.8)

        print(self.details, '393')

        for i, e in enumerate(self.details):
            self.del_list.insert(i, e[0])

    def Delete_task(self, entry):

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.c.execute("DELETE FROM frames WHERE tasks='{}'".format(entry))

        self.database.commit()
        self.database.close()

        for e in self.details:
            self.file.delete(e[0])

        self.details = []

        self.Retrive_catagories()

        # self.Home()

        self.del_wind.destroy()

    def Profile(self):

        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS name(
                                First_name TEXT,
                                Last_name TEXT 
                                )""")

        self.user = self.c.execute('SELECT * FROM name').fetchall()

        self.database.commit()
        self.database.close()
        self.lname = Label(self.root, text="", font=('helvatica', 10, 'bold italic'))
        # self.canvas_home.create_window(100, 245, anchor=CENTER, window=self.lname)

        # if len(self.user)<1:
        #   self.name=Label(self.root,text="Welcome,\nYour Name",font=('helvatica',20,'bold italic'),bg='#f3f3f3')
        #   self.canvas_home.create_window(100,200,anchor=CENTER,window=self.name)

        '''
        else:
            self.name = Label(self.root, text="Welcome,\n{}".format(self.user[0][0]), font=('helvatica', 20, 'bold italic'),bg='#f3f3f3')
            self.canvas_home.create_window(100, 200, anchor=CENTER, window=self.name)


        if len(self.user)>0:
            if len(self.user[0][1])>3:
                self.lname.config(text=self.user[0][1])
        '''

    def Profile_name(self):

        self.name_wind = Toplevel()
        self.name_wind.title('Your Name')
        self.name_wind.geometry('300x300+150+150')

        Label(self.name_wind, text='Provide Your Name! ', font=('', 16, 'bold'), fg='Gold').place(relx=0.05, rely=0.05)

        f_name = Entry(self.name_wind, width=20)
        f_name.place(relx=0.2, rely=0.4)

        l_name = Entry(self.name_wind, width=20)
        l_name.place(relx=0.2, rely=0.7)

        Label(self.name_wind, text="First Name :", font=(',14')).place(relx=0.2, rely=0.3)
        Label(self.name_wind, text="Last Name :", font=(',14')).place(relx=0.2, rely=0.55)

        btn = Button(self.name_wind, text="Submit", command=lambda: self.name_change(f_name.get(), l_name.get()))
        btn.place(relx=0.4, rely=0.85)

    def name_change(self, f_name, l_name):
        self.database = sqlite3.connect("DO_Not_Delete.db")
        self.c = self.database.cursor()

        if len(self.user) < 1:
            self.c.execute('INSERT INTO name VALUES ("{}","{}")'.format(f_name, l_name))

        else:
            self.c.execute('UPDATE name SET First_name="{}", Last_Name="{}" WHERE oid=1 '.format(f_name, l_name))
        self.database.commit()
        self.database.close()
        self.name_wind.destroy()

        self.name.config(text="Welcome,\n{}".format(f_name))

        if len(l_name) > 3:
            self.lname.config(text=l_name)
        else:
            self.lname.config(text='      ')


k = Menu_Class(root)

root.mainloop()
