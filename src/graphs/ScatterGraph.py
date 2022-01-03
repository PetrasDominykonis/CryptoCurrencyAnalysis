import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from database.sqlite_main import fetch_data_from_db
import numpy as np
import json
from pandas.plotting import autocorrelation_plot

config_file_path = '../src/config/cfg.json'

def draw_graph(selection, type, fromdate, todate):
    list = []
    list.append(selection)
    db_table,selection_name= find_by_index(selection)
    if db_table == "crypto_price_history":
        if type == 1:
            DF1 = fetch_data_from_db(db_table,list,fromdate,todate)
            DF2 = fetch_data_from_db(db_table,["BTC"],fromdate,todate)
            display_graph(DF1,DF2,selection,"BTC",f"{selection_name} kainos",f"Bitcoin kainos",["kainos","kainos"])
        elif type == 2:
            DF1 = fetch_data_from_db(db_table,list,fromdate,todate)
            DF2 = fetch_data_from_db("crypto_volume_history",list,fromdate,todate)
            display_graph(DF1,DF2,selection,selection,f"{selection_name} kainos",f"{selection_name} normalizuoti pardavimų kiekiai",["kainos","pardavimų kiekių"])

    if db_table == "stocks_price_history":
        if type == 1:
            DF1 = fetch_data_from_db(db_table,list,fromdate,todate)
            DF2 = fetch_data_from_db("crypto_price_history",["BTC"],fromdate,todate)
            display_graph(DF1,DF2,selection,"BTC",f"Prices of {selection}",f"Prices of BTC",["kainos","kainos"])
        if type == 2:
            DF1 = fetch_data_from_db(db_table,list,fromdate,todate)
            DF2 = fetch_data_from_db("stocks_volume_history",list,fromdate,todate)
            display_graph(DF1,DF2,selection,selection,f"{selection} kainos",f"{selection} normalizuoti pardavimų kiekiai",["kainos","pardavimų kiekių"])

def find_by_index(selection):
    config_data = json.load(open(config_file_path))
    for crypto in config_data['crypto_list']:
        if crypto['db_index']==selection:
            return "crypto_price_history",crypto['name']
    for stock in config_data['stocks_list']:
        if stock['db_index']==selection:
            return "stocks_price_history",crypto['name']

def display_graph(DF1, DF2, colname1, colname2, display_name1, display_name2, titles):
    plt.style.use('seaborn')
    plt.figure(f"{colname1} {titles[0]} ir {colname2} {titles[1]} sklaidos diagrama",figsize=(9.0,6.0))
    plt.title(f"{colname1} {titles[0]} ir {colname2} {titles[1]} sklaidos diagrama")
    DF1 = DF1.rename(columns={colname1:'temp'})
    CombDF = pd.merge(DF1,DF2,how='outer',on='date')
    CombDF = CombDF.dropna()
    plt.xlabel(display_name1)
    plt.ylabel(display_name2)
    plt.scatter(CombDF['temp'],CombDF[colname2],edgecolors='green',linewidths=1,alpha=0.75)
    plt.tight_layout
    plt.show()
