from tkinter import *
import random

from matplotlib.pyplot import text

root = Tk(className="this is a new classname")
root.geometry("800x800")

def randomNumber():
    return random.random()


def myClick():
    print("BUTTON CLICKED")
    myLabel1.config(text=randomNumber(), padx=200)

# Creating a Label Widget (Label) and Shoving it onto the screen (grid)
myLabel1 = Label(root, text="Label1")
myLabel1.grid(row=1,column=1)
myLabel2 = Label(root, text="Label2").grid(row=1, column=2)
myLabel3 = Label(root, text="Label3").grid(row=2, column=2)

myButton = Button(root, text="Click me!", padx=50, pady=50, command=myClick)
myButton.grid(row=3, column=1, padx = 200)



root.mainloop()