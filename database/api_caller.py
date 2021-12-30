import pandas_datareader as pd
import datetime as dt 
import json


currency = 'USD'
config_data = json.load(open('../config/cfg.json'))

def pull_crypto_data_from_api(start=dt.date(2015,1,1), end=dt.date.today()):
    first = True
    for crypto in config_data['crypto_list']:
        print(f"Pulling following crypto data -> {crypto}")
        data = pd.DataReader(f"{crypto['api_index']}-{currency}", 'yahoo' , start , end)
        if first:
            combined_prices = data[["Close"]].copy()
            combined_prices = combined_prices.rename(columns={"Close": crypto['db_index']})
            combined_volume = data[["Volume"]].copy()
            combined_volume = combined_volume.rename(columns={"Volume": crypto['db_index']})
            first = False
        else:
            combined_prices = combined_prices.join(data["Close"])
            combined_prices = combined_prices.rename(columns={"Close": crypto['db_index']})
            combined_volume = combined_volume.join(data["Volume"])
            combined_volume = combined_volume.rename(columns={"Volume": crypto['db_index']})
    return combined_prices, combined_volume

def pull_stocks_data_from_api(start=dt.date(2015,1,1), end=dt.date.today()):
    first = True
    for stock in config_data['stocks_list']:
        print(f"Pulling following stock data -> {stock}")
        data = pd.DataReader(f"{stock['api_index']}", 'yahoo' , start , end)
        if first:
            combined_prices = data[["Close"]].copy()
            combined_prices = combined_prices.rename(columns={"Close": stock['db_index']})
            combined_volume = data[["Volume"]].copy()
            combined_volume = combined_volume.rename(columns={"Volume": stock['db_index']})
            first = False
        else:
            combined_prices = combined_prices.join(data["Close"])
            combined_prices = combined_prices.rename(columns={"Close": stock['db_index']})
            combined_volume = combined_volume.join(data["Volume"])
            combined_volume = combined_volume.rename(columns={"Volume": stock['db_index']})
    return combined_prices, combined_volume