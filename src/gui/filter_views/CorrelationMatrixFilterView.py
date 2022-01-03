from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from graphs.CorrelationMatrixGraph import draw_graph
from datetime import timedelta as td
import datetime as dt

class CorrelationMatrixFilterView:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.frame.grid_propagate(0)

        #Checkbox variables for crypto
        self.BTCVAR = IntVar()
        self.ETHVAR = IntVar()
        self.BNBVAR = IntVar()
        self.USDTVAR = IntVar()
        self.SOLVAR = IntVar()
        self.XRPVAR = IntVar()
        self.ADAVAR = IntVar()
        self.USDCVAR = IntVar()
        self.AVAXVAR = IntVar()
        self.DOTVAR = IntVar()
        self.DOGEVAR = IntVar()
        self.MATICVAR = IntVar()
        self.CROVAR = IntVar()
        self.LTCVAR = IntVar()
        self.LINKVAR = IntVar()

        #Checkbox variables for stocks
        self.XAUVAR = IntVar()
        self.GSPCVAR = IntVar()
        self.TSLAVAR = IntVar()
        self.AAPLVAR = IntVar()
        self.MSFTVAR = IntVar()
        self.AMZNVAR = IntVar()
        self.PFEVAR = IntVar()

        #Radio buttons variable
        self.GraphTypeValue = IntVar()
        self.GraphTypeValue.set(1)

        
        #Start of crypto checkboxes
        self.label1 = Label(self.frame, text="Pasirinkite norimas kriptovaliutas:",anchor="w",height=2,width=30)
        self.label1.grid(row=0,column=1,columnspan=10,padx=20, pady=10)

        self.BTC_CB = Checkbutton(self.frame, text="Bitcoin",height=1,width=15,variable=self.BTCVAR)
        self.BTC_CB.grid(row=1,column=1,padx=10, pady=10)

        self.ETH_CB = Checkbutton(self.frame, text="Ethereum",height=1,width=15,variable=self.ETHVAR)
        self.ETH_CB.grid(row=1,column=2,padx=10, pady=10)

        self.BNB_CB = Checkbutton(self.frame, text="Binance Coin",height=1,width=15,variable=self.BNBVAR)
        self.BNB_CB.grid(row=1,column=3,padx=10, pady=10)

        self.USDT_CB = Checkbutton(self.frame, text="Tether",height=1,width=15,variable=self.USDTVAR)
        self.USDT_CB.grid(row=1,column=4,padx=10, pady=10)

        self.SOL_CB = Checkbutton(self.frame, text="Solana",height=1,width=15,variable=self.SOLVAR)
        self.SOL_CB.grid(row=1,column=5,padx=10, pady=10)

        self.XRP_CB = Checkbutton(self.frame, text="Ripple",height=1,width=15,variable=self.XRPVAR)
        self.XRP_CB.grid(row=1,column=6,padx=10, pady=10)

        self.ADA_CB = Checkbutton(self.frame, text="Cardano",height=1,width=15,variable=self.ADAVAR)
        self.ADA_CB.grid(row=2,column=1,padx=10, pady=10)

        self.USDC_CB = Checkbutton(self.frame, text="USD Coin",height=1,width=15,variable=self.USDCVAR)
        self.USDC_CB.grid(row=2,column=2,padx=10, pady=10)

        self.AVAX_CB = Checkbutton(self.frame, text="Avalanche",height=1,width=15,variable=self.AVAXVAR)
        self.AVAX_CB.grid(row=2,column=3,padx=10, pady=10)

        self.DOT_CB = Checkbutton(self.frame, text="Polkadot",height=1,width=15,variable=self.DOTVAR)
        self.DOT_CB.grid(row=2,column=4,padx=10, pady=10)

        self.DOGE_CB = Checkbutton(self.frame, text="Dogecoin",height=1,width=15,variable=self.DOGEVAR)
        self.DOGE_CB.grid(row=2,column=5,padx=10, pady=10)

        self.MATIC_CB = Checkbutton(self.frame, text="Polygon",height=1,width=15,variable=self.MATICVAR)
        self.MATIC_CB.grid(row=2,column=6,padx=10, pady=10)

        self.CRO_CB = Checkbutton(self.frame, text="Crypto.com Coin",height=1,width=15,variable=self.CROVAR)
        self.CRO_CB.grid(row=3,column=1,padx=10, pady=10)

        self.LTC_CB = Checkbutton(self.frame, text="Litecoin",height=1,width=15,variable=self.LTCVAR)
        self.LTC_CB.grid(row=3,column=2,padx=10, pady=10)

        self.LINK_CB = Checkbutton(self.frame, text="Chainlink",height=1,width=15,variable=self.LINKVAR)
        self.LINK_CB.grid(row=3,column=3,padx=10, pady=10)

        #Start of stocks checkboxes

        self.label2 = Label(self.frame, text="Pasirinkite norimas rinkas (kompanijas):",anchor="w",height=2,width=30)
        self.label2.grid(row=4,column=1,columnspan=10,padx=20, pady=10)

        self.XAU_CB = Checkbutton(self.frame, text="Aukso indeksas",height=1,width=15,variable=self.XAUVAR)
        self.XAU_CB.grid(row=5,column=1,padx=5, pady=10)

        self.GSPC_CB = Checkbutton(self.frame, text="S&P500",height=1,width=15,variable=self.GSPCVAR)
        self.GSPC_CB.grid(row=5,column=2,padx=5, pady=10)

        self.TSLA_CB = Checkbutton(self.frame, text="Tesla",height=1,width=15,variable=self.TSLAVAR)
        self.TSLA_CB.grid(row=5,column=3,padx=5, pady=10)

        self.AAPL_CB = Checkbutton(self.frame, text="Apple",height=1,width=15,variable=self.AAPLVAR)
        self.AAPL_CB.grid(row=5,column=4,padx=5, pady=10)

        self.MSFT_CB = Checkbutton(self.frame, text="Microsoft",height=1,width=15,variable=self.MSFTVAR)
        self.MSFT_CB.grid(row=6,column=1,padx=5, pady=10)

        self.AMZN_CB = Checkbutton(self.frame, text="Amazon",height=1,width=15,variable=self.AMZNVAR)
        self.AMZN_CB.grid(row=6,column=2,padx=5, pady=10)

        self.PFE_CB = Checkbutton(self.frame, text="Pfizer",height=1,width=15,variable=self.PFEVAR)
        self.PFE_CB.grid(row=6,column=3,padx=5, pady=10)

        #Start of graph type selection

        self.label3 = Label(self.frame, text="Pasirinkite diagramos tipą:",anchor="w",height=2,width=30)
        self.label3.grid(row=7,column=1,columnspan=10,padx=20, pady=10)

        self.Prices_RB = Radiobutton(self.frame, text="Kainų koreliacija", variable=self.GraphTypeValue, value=1)
        self.Prices_RB.grid(row=8,column=1,padx=5, pady=10)

        self.Volumes_RB = Radiobutton(self.frame, text="Kiekių koreliacija", variable=self.GraphTypeValue, value=2)
        self.Volumes_RB.grid(row=8,column=2,padx=5, pady=10)

        # self.Norm_RB = Radiobutton(self.frame, text="Normalizuotas grafikas", variable=self.GraphTypeValue, value=3)
        # self.Norm_RB.grid(row=8,column=3,padx=5, pady=10)

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
        self.GraphCallButton = Button(self.frame, text="Rodyti grafiką", height=2, width=20, command=self.GraphCallFunction)
        self.GraphCallButton.grid(row=10,column=5,columnspan=2,padx=20, pady=10)

    def GraphCallFunction(self):
        crypto_list = []
        if self.BTCVAR.get():
            crypto_list.append("BTC")
        if self.ETHVAR.get():
            crypto_list.append("ETH")
        if self.BNBVAR.get():
            crypto_list.append("BNB")
        if self.USDTVAR.get():
            crypto_list.append("USDT")
        if self.SOLVAR.get():
            crypto_list.append("SOL")
        if self.XRPVAR.get():
            crypto_list.append("XRP")
        if self.ADAVAR.get():
            crypto_list.append("ADA")
        if self.USDCVAR.get():
            crypto_list.append("USDC")
        if self.AVAXVAR.get():
            crypto_list.append("AVAX")
        if self.DOTVAR.get():
            crypto_list.append("DOT")
        if self.DOGEVAR.get():
            crypto_list.append("DOGE")
        if self.MATICVAR.get():
            crypto_list.append("MATIC")
        if self.CROVAR.get():
            crypto_list.append("CRO")
        if self.LTCVAR.get():
            crypto_list.append("LTC")
        if self.LINKVAR.get():
            crypto_list.append("LINK")

        stocks_list = []
        if self.XAUVAR.get():
            stocks_list.append("XAU")
        if self.GSPCVAR.get():
            stocks_list.append("GSPC")
        if self.TSLAVAR.get():
            stocks_list.append("TSLA")
        if self.AAPLVAR.get():
            stocks_list.append("AAPL")
        if self.MSFTVAR.get():
            stocks_list.append("MSFT")
        if self.AMZNVAR.get():
            stocks_list.append("AMZN")
        if self.PFEVAR.get():
            stocks_list.append("PFE")
        
        if crypto_list or stocks_list:
            draw_graph(crypto_list,stocks_list,self.GraphTypeValue.get(),self.DFromCal.get_date(),self.DToCal.get_date())
        else:
            messagebox.showerror(title=None,message="Pasirinkite bent vieną kriptovaliutą arba rinką")