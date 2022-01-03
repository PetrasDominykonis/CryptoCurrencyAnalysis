import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from database.sqlite_main import fetch_data_from_db
import numpy as np

def draw_graph(crypto_list, stocks_list, type, fromdate, todate):
    if crypto_list:
        CryptoDF = fetch_data_from_db("crypto_volume_history",crypto_list,fromdate,todate)
    if stocks_list:
        StocksDF = fetch_data_from_db("stocks_volume_history",stocks_list,fromdate,todate)
    if crypto_list and stocks_list:
        CombDF = pd.merge(CryptoDF,StocksDF,how='outer',on='date')
        CombDF = CombDF.dropna()
        comb_list = np.concatenate((crypto_list, stocks_list))

    elif crypto_list and not stocks_list:
        CombDF = CryptoDF
        CombDF = CombDF.dropna()
        comb_list = crypto_list
    elif stocks_list and not crypto_list:
        CombDF = StocksDF
        CombDF = CombDF.dropna()
        comb_list = stocks_list
    else:
        print("Missing data in PriceGraph -> draw_graph")

    CombDF['date'] = [dt.datetime.strptime(d,'%Y-%m-%d %H:%M:%S.%f').date() for d in CombDF['date']]

    plt.figure("Prekybos kiekių diagrama",figsize=(9.0,6.0))
    plt.title("Prekybos kiekių diagrama")
    plt.xlabel("Data")
    
    if type==2:
        plt.yscale('log')
        plt.ylabel("Prekybos kiekiai(logaritminė funkcija)")

    
    if type==3:
        plt.ylabel("Prekybos kiekiai(normalizuoti)")
        for item in comb_list:
            cmax= max(CombDF[item])
            cmin= min(CombDF[item])
            CombDF[item] = [(c-cmin)/(cmax-cmin) for c in CombDF[item]]
            plt.plot(CombDF['date'],CombDF[item], label = item)
    else:
        plt.ylabel("Prekybos kiekiai")
        for item in comb_list:
            plt.plot(CombDF['date'],CombDF[item], label = item)
    plt.grid()
    plt.style.use("seaborn")
    plt.legend(loc = "upper right")
    plt.show()

