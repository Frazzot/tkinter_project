# Bank, inventory, profile, sorting system, items
from tkinter import Frame, Tk, Menu, BOTH, Entry, StringVar, Button

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.__init__ = master
        self.init_window()

    def init_window(self):
        self.master.title("Tkinter Project")
        self.pack(fill=BOTH, expand=1)
        # self.grid(row=0, column=0, sticky="nsew")

        menu = Menu(self.master)
        self.master.config(menu=menu)

        users = Menu(menu, tearoff=0)
        users.add_command(label="Bank")
        users.add_command(label="Inventory")
        users.add_command(label="Profile")
        users.add_command(label="Create account")
        menu.add_cascade(label="Users", menu=users)

        store = Menu(menu, tearoff=0)
        store.add_command(label="Sell")
        store.add_command(label="Purchase")
        menu.add_cascade(label="Store", menu=store)
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
    
root = Tk()





root.geometry("600x500")
app = Window(root)
root.mainloop()

#TODO: Add entrys and stringvars plus login button