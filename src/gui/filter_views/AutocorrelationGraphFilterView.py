from tkinter import *
from matplotlib import widgets
from tkcalendar import *
from graphs.AutocorrelationGraph import draw_graph
from datetime import timedelta as td
import datetime as dt

class AutocorrelationGraphView:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.frame.grid_propagate(0)

        #Radio buttons variables
        self.RadioButtonSelection = StringVar()
        self.RadioButtonSelection.set("BTC")

        #Start of crypto radio buttons
        self.label1 = Label(self.frame, text="Pasirinkite norimą kriptovaliutą / rinką (kompaniją):",anchor="w",height=2,width=40)
        self.label1.grid(row=0,column=1,columnspan=10,padx=20, pady=10)

        self.BTC_RB = Radiobutton(self.frame, text="Bitcoin",height=1,width=15,variable=self.RadioButtonSelection, value="BTC")
        self.BTC_RB.grid(row=1,column=1,padx=10, pady=10)

        self.ETH_RB = Radiobutton(self.frame, text="Ethereum",height=1,width=15,variable=self.RadioButtonSelection, value="ETH")
        self.ETH_RB.grid(row=1,column=2,padx=10, pady=10)

        self.BNB_RB = Radiobutton(self.frame, text="Binance Coin",height=1,width=15,variable=self.RadioButtonSelection, value="BNB")
        self.BNB_RB.grid(row=1,column=3,padx=10, pady=10)

        self.USDT_RB = Radiobutton(self.frame, text="Tether",height=1,width=15,variable=self.RadioButtonSelection,value="USDT")
        self.USDT_RB.grid(row=1,column=4,padx=10, pady=10)

        self.SOL_RB = Radiobutton(self.frame, text="Solana",height=1,width=15,variable=self.RadioButtonSelection,value="SOL")
        self.SOL_RB.grid(row=1,column=5,padx=10, pady=10)

        self.XRP_RB = Radiobutton(self.frame, text="Ripple",height=1,width=15,variable=self.RadioButtonSelection,value="XRP")
        self.XRP_RB.grid(row=1,column=6,padx=10, pady=10)

        self.ADA_RB = Radiobutton(self.frame, text="Cardano",height=1,width=15,variable=self.RadioButtonSelection,value="ADA")
        self.ADA_RB.grid(row=2,column=1,padx=10, pady=10)

        self.USDC_RB = Radiobutton(self.frame, text="USD Coin",height=1,width=15,variable=self.RadioButtonSelection,value="USDC")
        self.USDC_RB.grid(row=2,column=2,padx=10, pady=10)

        self.AVAX_RB = Radiobutton(self.frame, text="Avalanche",height=1,width=15,variable=self.RadioButtonSelection,value="AVAX")
        self.AVAX_RB.grid(row=2,column=3,padx=10, pady=10)

        self.DOT_RB = Radiobutton(self.frame, text="Polkadot",height=1,width=15,variable=self.RadioButtonSelection,value="DOT")
        self.DOT_RB.grid(row=2,column=4,padx=10, pady=10)

        self.DOGE_RB = Radiobutton(self.frame, text="Dogecoin",height=1,width=15,variable=self.RadioButtonSelection,value="DOGE")
        self.DOGE_RB.grid(row=2,column=5,padx=10, pady=10)

        self.MATIC_RB = Radiobutton(self.frame, text="Polygon",height=1,width=15,variable=self.RadioButtonSelection,value="MATIC")
        self.MATIC_RB.grid(row=2,column=6,padx=10, pady=10)

        self.CRO_RB = Radiobutton(self.frame, text="Crypto.com Coin",height=1,width=15,variable=self.RadioButtonSelection,value="CRO")
        self.CRO_RB.grid(row=3,column=1,padx=10, pady=10)

        self.LTC_RB = Radiobutton(self.frame, text="Litecoin",height=1,width=15,variable=self.RadioButtonSelection,value="LTC")
        self.LTC_RB.grid(row=3,column=2,padx=10, pady=10)

        self.LINK_RB = Radiobutton(self.frame, text="Chainlink",height=1,width=15,variable=self.RadioButtonSelection,value="LINK")
        self.LINK_RB.grid(row=3,column=3,padx=10, pady=10)

        #Start of stocks radio buttons
        self.XAU_RB = Radiobutton(self.frame, text="Aukso indeksas",height=1,width=15,variable=self.RadioButtonSelection,value="XAU")
        self.XAU_RB.grid(row=5,column=1,padx=5, pady=10)

        self.GSPC_RB = Radiobutton(self.frame, text="S&P500",height=1,width=15,variable=self.RadioButtonSelection,value="GSPC")
        self.GSPC_RB.grid(row=5,column=2,padx=5, pady=10)

        self.TSLA_RB = Radiobutton(self.frame, text="Tesla",height=1,width=15,variable=self.RadioButtonSelection,value="TSLA")
        self.TSLA_RB.grid(row=5,column=3,padx=5, pady=10)

        self.AAPL_RB = Radiobutton(self.frame, text="Apple",height=1,width=15,variable=self.RadioButtonSelection,value="AAPL")
        self.AAPL_RB.grid(row=5,column=4,padx=5, pady=10)

        self.MSFT_RB = Radiobutton(self.frame, text="Microsoft",height=1,width=15,variable=self.RadioButtonSelection,value="MSFT")
        self.MSFT_RB.grid(row=6,column=1,padx=5, pady=10)

        self.AMZN_RB = Radiobutton(self.frame, text="Amazon",height=1,width=15,variable=self.RadioButtonSelection,value="AMZN")
        self.AMZN_RB.grid(row=6,column=2,padx=5, pady=10)

        self.PFE_RB = Radiobutton(self.frame, text="Pfizer",height=1,width=15,variable=self.RadioButtonSelection,value="PFE")
        self.PFE_RB.grid(row=6,column=3,padx=5, pady=10)

        #Start of date selection
        self.label4 = Label(self.frame, text="Pasirinkite datą(nuo):",anchor="w",height=2,width=30)
        self.label4.grid(row=9,column=1,columnspan=2,padx=20, pady=10)

        self.label5 = Label(self.frame, text="Pasirinkite datą(iki):",anchor="w",height=2,width=30)
        self.label5.grid(row=9,column=3,columnspan=2,padx=20, pady=10)

        DFromCalMaxDate = dt.date.today() - td(days=5)

        self.DFromCal = Calendar(self.frame, selectmode="day", year=DFromCalMaxDate.year,
                                month=DFromCalMaxDate.month,day=DFromCalMaxDate.day, maxdate=DFromCalMaxDate,
                                date_pattern="y-mm-dd",foreground="#000000",selectforeground="#ff0000")
        self.DFromCal.grid(row=10,column=1,columnspan=2,padx=20, pady=10)
        
        self.DToCal = Calendar(self.frame, selectmode="day", maxdate=dt.date.today(),date_pattern="y-mm-dd",foreground="#000000",selectforeground="#ff0000")
        self.DToCal.grid(row=10,column=3,columnspan=2,padx=20, pady=10)

        #Graph function call button
        self.GraphCallButton = Button(self.frame, text="Rodyti grafiką", height=2, width=20, command=self.InstructionsButtonFuncton)
        self.GraphCallButton.grid(row=10,column=5,columnspan=2,padx=20, pady=10)

    def InstructionsButtonFuncton(self):
        draw_graph(self.RadioButtonSelection.get(),
                   self.DFromCal.get_date(),
                   self.DToCal.get_date())