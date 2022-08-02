from tkinter import *
import tkinter as tk

import student_tracking_gui
import student_tracking_func



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,350)
        self.master.maxsize(500,350)

        self.master.title("Student Tracking Assignment")
        self.master.configure(bg="#F0F0F0")

        student_tracking_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
