import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from database.sqlite_main import fetch_data_from_db
import numpy as np
import mplfinance as mpf
import seaborn as sns

def draw_graph(crypto_list, stocks_list, type, fromdate, todate):
    if crypto_list:
        if type==1:
            CryptoDF = fetch_data_from_db("crypto_price_history",crypto_list,fromdate,todate)
        if type==2:
            CryptoDF = fetch_data_from_db("crypto_volume_history",crypto_list,fromdate,todate)
    if stocks_list:
        if type==1:
            StocksDF = fetch_data_from_db("stocks_price_history",stocks_list,fromdate,todate)
        if type==2:
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

    if type == 1:
        plt.figure("Kainų koreliacijų diagrama",figsize=(9.0,6.0))
        plt.title("Kainų koreliacijų diagrama")

    if type == 2:
        plt.figure("Kiekių koreliacijų diagrama",figsize=(9.0,6.0))
        plt.title("Kiekių koreliacijų diagrama")

    CombDF.drop(['date'],inplace=True,axis=1)
    CombDF = CombDF.pct_change().corr(method="pearson")
    sns.heatmap(CombDF, annot=True, cmap="coolwarm")
    plt.show()

