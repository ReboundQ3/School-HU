
#%%
#Steam_Stat_Grabber.py

import os
import sqlite3
import pprint

from os import path
from datetime import date
from datetime import datetime


# Datum van vandaag ophalen 
vandaag = datetime.now()
vandaag_afgk = vandaag.strftime("%d/%m/%Y %H:%M")
print(vandaag_afgk)

# SQLite DB checker
if path.exists("steamdb.db"):
    print("> STEAM DB CONNECTED")
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
else:
    print("> STEAM DB DOES NOT EXIST")

# DB_CUR.execute("DELETE FROM tbl_stats")
# DB_CUR.execute("INSERT INTO tbl_stats(game_id, game_name) SELECT game_id, game_name FROM tbl_games")
# DB_CUR.execute("UPDATE tbl_stats SET date = (?)", (vandaag_afgk,)), "WHERE date is NULL"
# DB_CON.commit()

gameslist_in = DB_CUR.execute("SELECT game_id, game_name from tbl_games")
gameslist_out = dict(gameslist_in)
pprint.pprint(dict(gameslist_out))
for game in gameslist_out:
    game_id  = game
    game_name = gameslist_out[game]
    playercount = "891398" # Ophalen via api
    DB_CUR.execute("INSERT INTO tbl_stats(date, game_id, game_name, playercount) VALUES (?, ?, ?, ?)", (vandaag_afgk, game_id, game_name, playercount))
# %%
