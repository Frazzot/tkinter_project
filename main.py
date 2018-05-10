# Bank, inventory, profile, sorting system, items
from tkinter import Frame, Tk, Menu, BOTH, Entry, StringVar, Button

class MyMenu(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.__init__ = master
        self.menu()
        self.frames = [Login_window(self), Ca_window(self)]

    def menu(self):
        self.master.title("Tkinter Project")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        users = Menu(menu, tearoff=0)
        users.add_command(label="Bank")
        users.add_command(label="Inventory")
        users.add_command(label="Profile")
        users.add_command(label="Create account", command=lambda: self.show_frame(1))
        menu.add_cascade(label="Users", menu=users)

        store = Menu(menu, tearoff=0)
        store.add_command(label="Sell")
        store.add_command(label="Purchase")
        menu.add_cascade(label="Store", menu=store)
    
    def show_frame(self, i):
        for x in range(len(self.frames)):
            if x != i:
                self.frames[x].pack_forget()
        self.frames[i].pack()


class Login_window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_window()

    def init_window(self):
        #self.master.title("Tkinter Project")
        self.pack(fill=BOTH, expand=1)
        username_holder = StringVar()
        password_holder = StringVar()
        b = Button(self, text="Login", command=self.callback)
        e1 = Entry(self, textvariable=username_holder)
        e2 = Entry(self,textvariable=password_holder)
        username_holder.set("Username")
        password_holder.set("Password")
        e1.pack()
        e2.pack()
        b.pack()
  
    def callback(self):
        print("click!")
    
class Ca_window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.__init__ = master
        self.init_ca_window()

    def init_ca_window(self, master=None):
        # self.master.title("Tkinter Project")
        self.pack(fill=BOTH, expand=1)
        username_holder = StringVar()
        password_holder = StringVar()
        b = Button(self, text="Create Account")
        e1 = Entry(self, textvariable=username_holder)
        e2 = Entry(self,textvariable=password_holder)
        username_holder.set("Username")
        password_holder.set("Password")
        e1.pack()
        e2.pack()
        b.pack()


root = Tk()
root.title("Tkinter project")
root.geometry("600x500")
app = MyMenu(root)
app.show_frame(0)
root.mainloop()

#TODO: New frame class for the menu