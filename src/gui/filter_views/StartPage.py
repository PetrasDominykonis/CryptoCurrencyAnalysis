from tkinter import *

class StartPage:

	def __init__(self, root, frame):
		self.root = root
		frame = frame
		frame.grid_propagate(0)
		self.label1 = Label(frame, text="Naudojimosi instrukcija:\n",anchor="w",height=3,width=20)
		self.label1.grid(row=1,column=1,columnspan=10,padx=300, pady=10)
		self.label2 = Label(frame, text="1. Kairėje esančiame meniu pasirinkite norimą įrankį(grafiką).",anchor="w",height=3,width=70)
		self.label2.grid(row=2,column=1,pady=20,padx=10)
		self.label3 = Label(frame, text="2. Dešinėje atsiradusiame meniu pasirinkite norimus filtrus.",anchor="w",height=3,width=70)
		self.label3.grid(row=3,column=1,pady=20,padx=10)
		self.label3 = Label(frame, text="3. Norint atsidaryti grafiką, paspauskite dešinėje apačioje esantį mygtuką.",anchor="w",height=3,width=70)
		self.label3.grid(row=4,column=1,pady=20,padx=10)
		self.label4 = Label(frame, text="4. Norint grįžti į instrukcijų puslapį paspauskite \"Instrukcijos\" mygtuką kairėje esančiame meniu.",anchor="w",height=3,width=70)
		self.label4.grid(row=5,column=1,pady=20,padx=10)
