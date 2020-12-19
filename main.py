from tkinter import *
from NotedCanvas import NotedCanvas
from Sidebar import Sidebar
from Mainview import Mainview

application = Tk()
application.title("D&D Organiser")

sidebar = Sidebar(application)
mainview = Mainview(application)

notedCanvas = NotedCanvas(mainview.tk, sidebar)

application.mainloop()