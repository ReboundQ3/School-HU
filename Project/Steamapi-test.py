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


# Stellaris game Achievements
#url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json"
# Playerdata Koen's account (ReboundQ3)
#url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=3B9518C4F0770B32EC2AB7A6B635E077&steamids=76561198044252418&format=json"
# Featured items
#url = "http://store.steampowered.com/api/featuredcategories/?l=english"

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

url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?gameid="
response = urlopen(url)
data_json = json.loads(response.read())['applist']['apps']
i = 0
for item in data_json:
    #print(item)
    i += 1
print(i)



# print("===================================================================================================")

# # JSON DATA STAGE 2 | print de hele dict in pretty print
# pprint.pprint(data_json)
# print("===================================================================================================")

# # JSON DATA STAGE 3 | Print de steam naam van de player uit de dict in terminal
# pprint.pprint(data_json['response']['players'][0]['personaname'])
# print("===================================================================================================")

# # JSON DATA STAGE 4 | Opent plaatje van steamavatar in default fotobewerker
# steam_avatar_URL_GET = data_json['response']['players'][0]['avatarfull']
# steam_avatar_URL_OPEN = urlopen(steam_avatar_URL_GET)
# steam_avatar_URL_JPG = Image.open(steam_avatar_URL_OPEN)
# steam_avatar_URL_JPG.show()

# # JSON DATA STAGE 5 | Opent plaatje in terminal \o/ door middel van het downloaden van JPG en ruimt hem weer op
# #urllib.request.urlretrieve(steam_avatar_URL_GET, "avatar.jpg")
# #steam_avatar_URL_PIC = np.asarray(Image.open("avatar.jpg"))
# #pprint.pprint(repr(steam_avatar_URL_PIC))
# #print("===================================================================================================")
# #plt.axis('off')
# #steam_avatar_URL_SHOW = plt.imshow(steam_avatar_URL_PIC)
# # %%

# %%
