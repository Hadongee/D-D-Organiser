from tkinter import *

class Sidebar:
    def __init__ (self, parent):
        self.tk = Frame(parent, width=200, height=500)
        self.tk.pack(side=RIGHT, expand=False, fill=Y, anchor=NE)

    def edit_note_name (self, event=None):
        self.editing_note.edit_name(self.name.get())

    def show_note (self, note):
        self.editing_note = note
        self.label_title = StringVar()
        self.label_title.set("Edit Note")
        self.title = Label(self.tk, textvariable=self.label_title, width=30)
        self.title.grid(row=0)
        self.name = Entry(self.tk)
        self.name.insert(END, note.name)
        self.name.grid(row=1, column=0)
        self.name.bind('<Return>', self.edit_note_name)
        self.name_set = Button(self.tk, text="set", command=self.edit_note_name)
        self.name_set.grid(row=1, column=1)

    def cancel_note (self):
        self.label_title = None
        self.title.grid_remove()
        self.name.grid_remove()
        self.name_set.grid_remove()
        self.editing_note = None