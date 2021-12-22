from tkinter import *
from gui.MenuBar import *

class MainWindow:
   def __init__(self):
       self.root = Tk()
       self.root.wm_title("Cryptocurrency analysis system")
       self.root.config(background="#FFFFFF")
       self.root.geometry("900x700")
       self.menubar = MenuBar(self.root)

   def start(self):
      self.root.mainloop()