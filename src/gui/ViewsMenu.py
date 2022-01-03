from tkinter import *
from gui.filter_views.StartPage import *
from gui.filter_views.PriceGraphFilterView import *
from gui.filter_views.AutocorrelationGraphFilterView import *
from gui.filter_views.ScatterGraphFilterView import *
from gui.filter_views.VolumesGraphFilterView import *
from gui.filter_views.CorrelationMatrixFilterView import *

class ViewsMenu:

    def __init__(self, root, leftFrame):
        self.root = root
        self.leftFrame = leftFrame

        self.rightFrame = Frame(self.root, width=1000, height = 740, bg="#ffd9ab")
        self.rightFrame.grid(row=0, rowspan=70, column=1, columnspan=10, padx=10, pady=10)
        self.rightPanel = StartPage(self.root, self.rightFrame)

        self.label = Label(self.leftFrame, text="Įrankio pasirinkimas")
        self.label.grid(row=0, column=0)

        self.InstructionsButton = Button(self.leftFrame, text="Instrukcijos", height=3, width=30, command=self.InstructionsButtonFuncton)
        self.InstructionsButton.grid(row=1, column=0)

        self.PricesGraphButton = Button(self.leftFrame, text="Kainų diagrama", height=3, width=30, command=self.PricesGraphButtonFunction)
        self.PricesGraphButton.grid(row=2, column=0)

        self.AutoCorrelationGraphButton = Button(self.leftFrame, text="Autokoreliacijos diagrama", height=3, width=30, command=self.AutoCorrelationGraphButtonFunction)
        self.AutoCorrelationGraphButton.grid(row=3, column=0)

        self.ScatterPlotDiagramButton = Button(self.leftFrame, text="Sklaidos diagrama", height=3, width=30, command=self.ScatterPlotGraphButtonFunction)
        self.ScatterPlotDiagramButton.grid(row=4, column=0)
         
        self.CorrelationMatrixGraphButton = Button(self.leftFrame, text="Koreliacijų matrica", height=3, width=30, command=self.CorrelationMatrixGraphButtonFunction)
        self.CorrelationMatrixGraphButton.grid(row=5, column=0)
         
        self.VolumeGraphButton = Button(self.leftFrame, text="Prekybos kiekių diagrama", height=3, width=30, command=self.VolumeGraphButtonFunction)
        self.VolumeGraphButton.grid(row=6, column=0)
    

    def InstructionsButtonFuncton(self):
        self.rightFrame.destroy()
        self.rightFrame = Frame(self.root, width=1000, height = 740, bg="#ffd9ab")
        self.rightFrame.grid(row=0, rowspan=70, column=1, columnspan=10, padx=10, pady=10)
        self.rightPanel = StartPage(self.root, self.rightFrame)

    def PricesGraphButtonFunction(self):
        self.rightFrame.destroy()
        self.rightFrame = Frame(self.root, width=1000, height = 740, bg="#ffd9ab")
        self.rightFrame.grid(row=0, rowspan=70, column=1, columnspan=20, padx=10, pady=10)
        self.rightPanel = PriceGraphFilterView(self.root, self.rightFrame)

    def AutoCorrelationGraphButtonFunction(self):
        self.rightFrame.destroy()
        self.rightFrame = Frame(self.root, width=1000, height = 740, bg="#ffd9ab")
        self.rightFrame.grid(row=0, rowspan=70, column=1, columnspan=20, padx=10, pady=10)
        self.rightPanel = AutocorrelationGraphView(self.root, self.rightFrame)

    def ScatterPlotGraphButtonFunction(self):
        self.rightFrame.destroy()
        self.rightFrame = Frame(self.root, width=1000, height = 740, bg="#ffd9ab")
        self.rightFrame.grid(row=0, rowspan=70, column=1, columnspan=20, padx=10, pady=10)
        self.rightPanel = ScatterGraphView(self.root, self.rightFrame)

    def CorrelationMatrixGraphButtonFunction(self):
        self.rightFrame.destroy()
        self.rightFrame = Frame(self.root, width=1000, height = 740, bg="#ffd9ab")
        self.rightFrame.grid(row=0, rowspan=70, column=1, columnspan=20, padx=10, pady=10)
        self.rightPanel = CorrelationMatrixFilterView(self.root, self.rightFrame)

    def VolumeGraphButtonFunction(self):
        self.rightFrame.destroy()
        self.rightFrame = Frame(self.root, width=1000, height = 740, bg="#ffd9ab")
        self.rightFrame.grid(row=0, rowspan=70, column=1, columnspan=20, padx=10, pady=10)
        self.rightPanel = VolumesGraphFilterView(self.root, self.rightFrame)