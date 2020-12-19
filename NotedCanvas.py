from tkinter import *
from PIL import ImageTk, Image
from Note import Note

class NotedCanvas:
    def __init__ (self, parent, sidebar) :
        # TODO: Find a better way to do this, how to do constants in python?
        self.distance_for_select = 100
        self.sidebar = sidebar

        self.canvas = Canvas(parent, bg="#ccc", width=1000, height=800)
        self.image = ImageTk.PhotoImage(Image.open("world.jpg"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas.pack(expand=True, fill="both")

        self.notes = []

        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        self.canvas.bind("<ButtonPress-3>", self.add_marker)
        self.canvas.bind("<ButtonRelease-1>", self.select_marker)

    def move_start (self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def add_marker(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        note = Note(x, y, self.canvas)
        self.notes.append(note)
        self.sidebar.show_note(note)

    def select_marker(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        closest = None
        for note in self.notes:
            if (closest == None or note.square_distance_to(x, y) < closest.square_distance_to(x, y)) and (note.square_distance_to(x, y) <= self.distance_for_select):
                closest = note
        if closest != None:
            # TODO: Functionality for selecting a note for editting
            self.sidebar.show_note(closest)
        else:
            self.sidebar.cancel_note()