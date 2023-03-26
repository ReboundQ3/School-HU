#%%
# Steamapi-test.py V1.1
#
# STEAM API -> Json TEST
#
# Aan te raden om met Jypyter te runnen want dan print hij wat beter

# Alle imports

import urllib as url
import urllib.request
from urllib.request import urlopen
import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
from os import path
import sqlite3
from datetime import datetime

#> Datum van vandaag

today = datetime.now()
today_A = today.strftime("%d/%m/%Y %H:%M")
print(today_A)

# Koen Git credentials z6ugwyvaic3wp5ujr3ftullejjc3hs4aggdade3qrge32p2jhhpa
# Koen Token pybu6qltnuke3dxkbsd5m2thxzvqi2q6eal3flmmhigk3dse2b4q
steamToken = "F9DF95CC74A3D0C07A6A83C7D0C66F6A"
steamID = "76561198121931212"
APIUrl = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=" + steamToken +"&steamid=" + steamID +"&format=json"
# API RESPONSE CHECKER 200 == OK
respone_API = urlopen(APIUrl)
#print(respone_API.getcode())
respone_API_code = respone_API.getcode()

if respone_API_code == 200:
    print("> STEAM API OK CODE:", respone_API_code)
else:
    print("> STEAM API ERROR ", respone_API_code)

# > DB

print("==================================================================")

if path.exists("steamdb.db"):
    print("> STEAM DB ALREADY EXISTS SKIPPING")
    DB_CON = sqlite3.connect("steamdb.db")
    CUR = DB_CON.cursor()
else:
    print("> STEAM DB CREATED")
    DB_CON = sqlite3.connect("steamdb.db")
    CUR = DB_CON.cursor()
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

CUR.execute("DELETE FROM tbl_games")
for game in gamesToCheck:
    game_name = game
    game_id = gamesToCheck[game]
    CUR.execute("INSERT INTO tbl_games(game_id, game_name) VALUES (?, ?)",
                (game_id, game_name))
    DB_CON.commit()
    
# %%
