import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from database.sqlite_main import fetch_data_from_db
import numpy as np
import json
from pandas.plotting import autocorrelation_plot

config_file_path = '../src/config/cfg.json'

def draw_graph(selection, fromdate, todate):
    list = []
    list.append(selection)
    db_table,selection_name= find_by_index(selection)
    DF = fetch_data_from_db(db_table,list,fromdate,todate)
    DF['date'] = DF['date'].astype('datetime64')
    DF = DF.set_index('date')
    plt.figure(f"{selection_name} autokoreliacijos diagrama",figsize=(9.0,6.0))
    plt.title(f"{selection_name} autokoreliacijos diagrama")
    plt.xlabel("Lagas")
    plt.ylabel("Autokoreliacija")
    autocorrelation_plot(DF)
    plt.show()

def find_by_index(selection):
    config_data = json.load(open(config_file_path))
    for crypto in config_data['crypto_list']:
        if crypto['db_index']==selection:
            return "crypto_price_history",crypto['name']
    for stock in config_data['stocks_list']:
        if stock['db_index']==selection:
            return "stocks_price_history",crypto['name']