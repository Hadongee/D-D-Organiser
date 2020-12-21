from tkinter import *

class Note:
    def __init__ (self, x, y, canvas):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.name = "New Note"
        self.description = ""
        self.marker = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="white")
        self.text = canvas.create_text(x, y-15, text=self.name, font='TkMenuFont', justify='center')
        self.box = canvas.create_rectangle(canvas.bbox(self.text),fill="white")
        canvas.tag_lower(self.box, self.text)

    def edit_name (self, new_name):
        self.name = new_name
        self.canvas.itemconfig(self.text, text=self.name)
        self.canvas.coords(self.box, self.canvas.bbox(self.text))

    # Get square distance from note to another point
    def square_distance_to (self, x, y):
        return pow(x-self.x, 2) + pow(y-self.y, 2)

