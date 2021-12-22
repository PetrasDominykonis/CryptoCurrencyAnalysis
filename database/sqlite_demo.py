import sqlite3 as db

connect = db.connect('price_history.db')

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS price_history(
                    date text
              )""")

# Add a new column
try:
    cursor.execute("ALTER TABLE price_history ADD COLUMN BTC INTEGER")
except:
    pass
