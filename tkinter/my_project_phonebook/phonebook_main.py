# Python Ver: 3.10.5
#
# Author: Quinn Davis
#
# Purpose: Phonebook Demo. Learning OOP, Tkinter GUI module,
#          using Tkinter Parent and Child relationships.
#
# Tested OS: This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox


# import other modules
import phonebook_gui
import phonebook_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define the master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        # center the app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")

        # catch if the user clicks on the X
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load the GUI widges from the GUI module
        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
