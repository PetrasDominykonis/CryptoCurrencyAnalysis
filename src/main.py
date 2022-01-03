from gui.MainWindow import *
from database import sqlite_main as sqldb

# sqldb.create_tables()
# sqldb.refresh_crypto_db_data()
# sqldb.refresh_stocks_db_data()

mainWindow = MainWindow()
mainWindow.start()