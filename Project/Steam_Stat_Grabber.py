
#%%
#Steam_Stat_Grabber.py

# Import modules
import sqlite3
import pprint
import json
from os import path
from datetime import datetime
from urllib.request import urlopen

# Get current datetime in format: DD/MM/YYYY HH:MM
dateTime = datetime.now().strftime("%d/%m/%Y %H:%M")

# Check if SQLite DB exist and connect to it
if path.exists("steamdb.db"):
    print("> STEAM DB CONNECTED")
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
else:
    print("> STEAM DB DOES NOT EXIST")

# Define function to get playercount from API
def playerCount(gameID):
    playerCountURL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=" + str(gameID)
    response = urlopen(playerCountURL)
    players = json.loads(response.read())['response']['player_count']
    return players

# Get game IDs and names from tbl_games
gameList = dict(DB_CUR.execute("SELECT game_id, game_name from tbl_games"))

# Cleanup database
# DB_CUR.execute("DELETE FROM tbl_stats")

# Insert the collected stats into tbl_stats
for game in gameList:
    gameID  = game
    gameName = gameList[game]
    playercount = playerCount(gameID)
    
    sql = '''INSERT INTO tbl_stats(date, game_id, game_name, playercount)
        VALUES (?, ?, ?, ?)'''
    
    input = (dateTime, gameID, gameName, playercount)
    DB_CUR.execute(sql, input)
    DB_CON.commit()



