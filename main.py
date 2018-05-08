# Bank, inventory, profile, sorting system, items
from tkinter import Frame, Tk, Menu, BOTH

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.__init__ = master
        self.init_window()

    def init_window(self):
        self.master.title("Tkinter Project")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        users = Menu(menu, tearoff=0)
        users.add_command(label="Log in")
        menu.add_cascade(label="Users", menu=users)


root = Tk()
root.geometry("1000x600")
app = Window(root)
root.mainloop()