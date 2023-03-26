
#%%
#Steam_Stat_Grabber.py

import os
import sqlite3

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

gameslist = DB_CUR.execute("SELECT game_id, game_name from tbl_games")
for game in gamelist:
    game_id  = game[0]
    game_name = game[1]
    playercount = "891398" # Ophalen via api
    DB_CUR.execute("INSERT INTO tbl_stats(Date,Game_id,Game_name,Playercount) VALUES", (vandaag_afgk,game_id,game_name,playercount))

game_id = DB_CUR.execute("SELECT game_id FROM tbl_stats;")
print(game_id)
# %%
