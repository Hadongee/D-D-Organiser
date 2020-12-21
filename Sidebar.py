from tkinter import *
from enum import Enum
from tkinter import scrolledtext

class SidebarState (Enum):
    Options = 1
    EditNote = 2

class Sidebar:
    def __init__ (self, parent):
        self.state = SidebarState.Options
        self.tk = Frame(parent, width=200, height=500)
        self.tk.pack(side=RIGHT, expand=False, fill=Y, anchor=NE)
        self.label_title = StringVar()
        self.label_title.set("Options")
        self.title = Label(self.tk, textvariable=self.label_title, width=30)
        self.title.grid(row=0)

    def edit_state (self, new_state):
        if self.state == SidebarState.EditNote:
            self.name.grid_remove()
            self.name_set.grid_remove()
            self.description.grid_remove()
            self.description_set.grid_remove()
            self.editing_note = None
        self.state = new_state
        if self.state == SidebarState.EditNote:
            self.label_title.set("Edit Note")
        if self.state == SidebarState.Options:
            self.label_title.set("Options")


    def edit_note_name (self, event=None):
        self.editing_note.edit_name(self.name.get())

    def edit_note_description (self, event=None):
        self.editing_note.description = self.description.get('1.0', 'end-1c')

    def show_note (self, note):
        self.cancel_note()
        self.edit_state(SidebarState.EditNote)
        self.editing_note = note
        self.name = Entry(self.tk)
        # Name
        self.name.insert(END, note.name)
        self.name.grid(row=1, column=0)
        self.name.bind('<Return>', self.edit_note_name)
        self.name_set = Button(self.tk, text="set", command=self.edit_note_name)
        self.name_set.grid(row=1, column=1)
        # Description
        self.description = scrolledtext.ScrolledText(self.tk, width=30, height=10)
        self.description.insert(END, note.description)
        self.description.grid(row=2, column=0)
        self.description_set = Button(self.tk, text="set", command=self.edit_note_description)
        self.description_set.grid(row=3, column=0)

    def cancel_note (self):
        if self.state == SidebarState.EditNote:
            self.edit_state(SidebarState.Options)