from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import sqlite3


class Main(Screen):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)
    contact = ObjectProperty(None)


    def getValues(self):
        self.firstname = self.first_name.text
        self.lastname = self.last_name.text
        self.email_1 = self.email.text
        self.contact_1 = self.contact.text
        print(self.firstname, self.lastname, self.email_1, self.contact_1)
        self.first_name.text = ''
        self.last_name.text = ''
        self.email.text = ''
        self.contact.text = ''
        db = sqlite3.connect('details.db')
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Info(
        
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        contact INTEGER
        )""")

        c.execute("""INSERT INTO Info(first_name,last_name,email,contact)VALUES(?,?,?,?)
        
        """, (self.firstname, self.lastname, self.email_1, self.contact_1))

        db.commit()
        db.close()
        self.sts.text="Account Created"

    # Creating content in python file is better than in kv file
    def EditPop(self):

        self.grid = GridLayout(rows=3,padding=10)

        self.grid.add_widget(Label(text="First Name :"))
        self.text = TextInput(multiline=False)
        self.grid.add_widget(self.text)
        popbtn = Button(text="search")
        self.grid.add_widget(popbtn)
        pop = Popup(title="Edit", content=self.grid, size_hint=(None, None), size=(300, 300))
        popbtn.bind(on_press=lambda x: self.pop(self.text.text), on_release=lambda x:pop.dismiss())
        pop.open()

        return self.text.text


    def pop(self, name):

        db = sqlite3.connect('details.db')
        c = db.cursor()
        self.details = c.execute('''SELECT * FROM Info WHERE first_name = '{}' '''.format(name)).fetchall()
        db.close()
        sm.current = 'Edit'
        return self.details


    def view(self):
        sm.current='view'


class Edit(Screen):


    def on_pre_enter(self, *args):

        self.edit_name=sm.screens[0].details

        if len(self.edit_name)>0:
            self.fn.text=self.edit_name[0][0]
            self.ln.text=self.edit_name[0][1]
            self.em.text=self.edit_name[0][2]
            self.con.text=str(self.edit_name[0][3])
        else:
            Editgrid = GridLayout(rows=3, padding=10)

            Editgrid.add_widget(Label(text='Your Name is not Registered in Database\nPlease Register!!!'))
            popbtn = Button(text="Ok")
            Editgrid.add_widget(popbtn)
            pop = Popup(title="Not Found", content=Editgrid, size_hint=(None, None), size=(400, 300))
            popbtn.bind( on_release=lambda x: pop.dismiss())
            pop.open()
            sm.current='login'
    def Save(self):
        db=sqlite3.connect('details.db')
        c=db.cursor()
        c.execute('''UPDATE Info set (first_name,last_name,email,contact)=('{}','{}','{}',{}) WHERE first_name='{}'
        '''.format(self.fn.text,self.ln.text,self.em.text,int(self.con.text),self.edit_name[0][0]))
        db.commit()
        db.close()
        sm.current='login'


class View(Screen):

    def on_pre_enter(self, *args):
        db=sqlite3.connect('details.db')
        c=db.cursor()
        det=c.execute("SELECT OID,* FROM Info").fetchall()
        print(det)
        self.m=GridLayout(rows=3)
        self.v=GridLayout(cols=3,padding=[-5,10,5,5])

        for e in det:
            self.v.add_widget(Label(text=str(e[0])))
            self.v.add_widget(Label(text=str(e[1])))
            self.v.add_widget(Label(text=str(e[2])))

        print(self.v.children)
        self.m.add_widget(self.v)
        self.m.add_widget(Button(text='View one', size_hint=[0, .1], on_press=lambda x: self.One()))
        self.m.add_widget(Button(text='Back',size_hint=[0,.1],on_press=lambda x:self.click()))

        self.add_widget(self.m)

    def click(self):
        sm.current='login'
    def One(self):
        self.grid = GridLayout(rows=3, padding=10)

        self.grid.add_widget(Label(text="First Name :"))
        self.text = TextInput(multiline=False)
        self.grid.add_widget(self.text)
        popbtn = Button(text="Show")
        self.grid.add_widget(popbtn)
        pop = Popup(title="View", content=self.grid, size_hint=(None, None), size=(200, 200))
        popbtn.bind(on_press=lambda x:self.leave(),on_release=lambda x: pop.dismiss())
        pop.open()
        return self.text

    def leave(self):
        sm.current='view2'


    def on_leave(self, *args):
        self.clear_widgets(self.children)


class View2(Screen):
    def on_pre_enter(self, *args):
        fname=sm.screens[2].text.text
        db = sqlite3.connect('details.db')
        c = db.cursor()
        self.view_details = c.execute('''SELECT * FROM Info WHERE first_name = '{}' '''.format(fname)).fetchall()
        db.close()
        print(self.view_details)
        self.fname_view.text=self.view_details[0][0]
        self.lname_view.text = self.view_details[0][1]
        self.email_view.text = self.view_details[0][2]
        self.contact_view.text = str(self.view_details[0][3])

class Manager(ScreenManager):
    pass


kv = Builder.load_file('Log.kv')

sm=ScreenManager()
class LoginApp(App):

    def build(self):
        self.icon = r"loginpage.png"
        sm.add_widget(Main())
        sm.add_widget(Edit())
        sm.add_widget(View())
        sm.add_widget(View2())

        return sm


LoginApp().run()
'''
GridLayout:
        rows:4
        size_hint:[0.8,0.8]
        pos_hint:{'x':.1,'top':1}
        edit:edit

'''
