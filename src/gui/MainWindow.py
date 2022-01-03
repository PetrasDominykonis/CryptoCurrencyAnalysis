from tkinter import *
from gui.MenuBar import *
from gui.ViewsMenu import *


class MainWindow:
   def __init__(self):
       self.root = Tk()
       self.root.wm_title("Kriptovaliutų analizės sistema")
       self.root.config(background="#bfbfbf")
       self.root.geometry('1366x768')
       self.menubar = MenuBar(self.root)
       self.leftFrame = Frame(self.root, width=300, height = 740, bg="#ffd9ab").grid(row=0,rowspan=7, column=0, padx=10, pady=10)
       self.ViewsMenu = ViewsMenu(self.root, self.leftFrame)
       

   def start(self):
      self.root.mainloop()