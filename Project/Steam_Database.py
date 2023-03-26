#%%
#Steam_Database.py
# Alle imports

import os
from os import path
import sqlite3

# > DB

print("==================================================================")

if path.exists("steamdb.db"):
    print("> STEAM DB ALREADY EXISTS SKIPPING")
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
else:
    print("> STEAM DB CREATED")
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
    DB_CON.execute("CREATE TABLE tbl_games(game_id, game_name)")
    DB_CON.execute("CREATE TABLE tbl_stats(date, game_id, game_name, playercount)")

print("==================================================================")

# RocketLeague, TF2, CS:GO, Terraria, Stellaris, BF 2042
gamesToCheck = {
    "RocketLeague" : 252950,
    "TF2" : 440, 
    "CS:GO" : 730,
    "Terria" : 105600,
    "Stellaris" : 281990,
    "BF2042" : 1517290
}

DB_CUR.execute("DELETE FROM tbl_games")
for game in gamesToCheck:
    game_name = game
    game_id = gamesToCheck[game]
    DB_CUR.execute("INSERT INTO tbl_games(game_id, game_name) VALUES (?, ?)",
                (game_id, game_name))
    DB_CON.commit()
    
# %%
