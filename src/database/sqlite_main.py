import sqlite3 as db
import json
import datetime as dt
from datetime import timedelta as td
import pandas as pd
from database.api_caller import pull_crypto_data_from_api, pull_stocks_data_from_api
from sqlalchemy import create_engine
from os.path import exists

db_file_path = '../src/database/price_history.db'
config_file_path = '../src/config/cfg.json'

def create_tables():
    config_data = json.load(open(config_file_path))
    connect = db.connect(db_file_path)
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS crypto_price_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date text UNIQUE
        )""")
    for crypto in config_data['crypto_list']:
        try:
            cursor.execute(f"ALTER TABLE crypto_price_history ADD COLUMN {crypto['db_index']} REAL")
        except:
            pass
    

    cursor.execute("""CREATE TABLE IF NOT EXISTS stocks_price_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date text UNIQUE
        )""")
    for stock in config_data["stocks_list"]:
        try:
            cursor.execute(f"ALTER TABLE stocks_price_history ADD COLUMN {stock['db_index']} REAL")
        except:
            pass

    cursor.execute("""CREATE TABLE IF NOT EXISTS crypto_volume_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date text UNIQUE
        )""")
    for crypto in config_data['crypto_list']:
        try:
            cursor.execute(f"ALTER TABLE crypto_volume_history ADD COLUMN {crypto['db_index']} INTEGER")
        except:
            pass

    cursor.execute("""CREATE TABLE IF NOT EXISTS stocks_volume_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date text UNIQUE
        )""")
    for stock in config_data["stocks_list"]:
        try:
            cursor.execute(f"ALTER TABLE stocks_volume_history ADD COLUMN {stock['db_index']} INTEGER")
        except:
            pass

    connect.commit()
    connect.close()

def refresh_crypto_db_data():
    table_name = "crypto_price_history"
    if exists(db_file_path):
        print('refresh_crypto_db_data -> file exists')
        last_id = get_last_table_row_id(table_name)
        if last_id != None:
            last_record = get_specific_row_by_id(table_name, last_id)
            last_day_recorded = string_to_date(last_record[1]).date()
            if last_day_recorded + td(days=1) < dt.date.today():
                prices_data, volume_data = pull_crypto_data_from_api(last_day_recorded + td(days=1), dt.date.today())
                add_data_to_db(table_name, prices_data)
                add_data_to_db('crypto_volume_history', volume_data)
                print("Crypto data was successfully refreshed")
            else:
                print("Crypto data is up to date")
        else:
            prices_data, volume_data = pull_crypto_data_from_api()
            add_data_to_db(table_name, prices_data)
            add_data_to_db('crypto_volume_history', volume_data)
            print("Crypto data was successfully refreshed")
    else:
        print("DB file does not exist")

def refresh_stocks_db_data():
    table_name = "stocks_price_history"
    if exists(db_file_path):
        print('refresh_stocks_db_data -> file exists')
        last_id = get_last_table_row_id(table_name)
        if last_id != None:
            last_record = get_specific_row_by_id(table_name, last_id)
            last_day_recorded = string_to_date(last_record[1]).date()
            if last_day_recorded + td(days=5) < dt.date.today():
                prices_data, volume_data = pull_stocks_data_from_api(last_day_recorded + td(days=1), dt.date.today())
                add_data_to_db('stocks_price_history', prices_data)
                add_data_to_db('stocks_volume_history', volume_data)
                print("Stocks data was successfully refreshed")
            else:
                print("Stocks data is up to date")
        else:
            prices_data, volume_data = pull_stocks_data_from_api()
            add_data_to_db(table_name, prices_data)
            add_data_to_db('stocks_volume_history', volume_data)
            print("Stocks data was successfully refreshed")
    else:
        print("DB file does not exist")

def fetch_data_from_db(table_name=None, items=None, start=None, end=None):
    if table_name==None:
        print("Missing table_name value in fetch_data_from_db function call")
        return None
    if items==None:
        print("Missing list values in fetch_data_from_db function call")
        return None
    timeframe = date_filter(start,end)
    connect = db.connect(db_file_path)
    print(f"""SELECT {columns_filter(items)} FROM {str(table_name)} {timeframe}""")
    results = pd.read_sql_query(f"""SELECT {columns_filter(items)} FROM {str(table_name)} {timeframe}""", connect)
    return results

def columns_filter(items):
    result = "date"
    for item in items:
        result += str(f",{item}")
    return str(result)

def date_filter(start, end):
    if start != None and end != None:
        result = f"WHERE date>date('{str(start)}') AND date<date('{str(end)}')"
        return result
    elif start != None and end==None:
        result = f"WHERE date>date('{str(start)}')"
        return result
    elif start == None and end!=None:
        result = f"WHERE date<date('{str(end)}')"
        return result
    else:
        print("No timeframe was selected, setting it to last year")
        return f"WHERE date>date('{dt.date.today() - td(days=365)}') AND date<date('{dt.date.today()}')"


def add_data_to_db(table_name, data):
    engine = create_engine(f"sqlite:///{db_file_path}", echo=False)
    data.to_sql(table_name, con=engine, if_exists='append')

def get_last_table_row_id(table_name):
    connect = db.connect(db_file_path)
    cursor = connect.cursor()
    last_id = cursor.execute(f"""SELECT max(id) FROM {table_name}""").fetchone()[0]
    connect.close()
    return last_id

def get_specific_row_by_id(table_name, record_id):
    connect = db.connect(db_file_path)
    cursor = connect.cursor()
    specific_record = cursor.execute(f"""SELECT * FROM {table_name} WHERE id={record_id}""").fetchone()
    connect.close()
    return specific_record

def string_to_date(string):
    return dt.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')

#---------------------------------------------------------------------------------------------------------------
# Test function for printing whole dataframe to file in case if program fails to save dataframe to DB
def write_whole_dataframe_to_file(dataframe):
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    with open('data.txt', 'w') as f:
        for item in dataframe:
            f.write(str(item)+"\n")
        f.write("\n")
        f.write(str(dataframe))