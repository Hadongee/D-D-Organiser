from tkinter import *

class Mainview:
    def __init__ (self, parent):
        self.tk = Frame(parent, width=1000, height=1000, bg="#555555")
        self.tk.pack(side=LEFT, expand=True, fill="both", anchor=W)