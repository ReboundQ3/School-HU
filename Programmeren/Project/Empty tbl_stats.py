
#%%
# Empty tbl_stats.py

# Import modules
import sqlite3
from os import path

# Check if SQLite DB exist and connect to it
if path.exists("steamdb.db"):
    print("> STEAM DB CONNECTED")
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
else:
    print("> STEAM DB DOES NOT EXIST")

DB_CUR.execute("DELETE FROM tbl_stats")
DB_CON.commit()