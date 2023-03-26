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
    print("> STEAM API OK")
else:
    print("> STEAM API ERROR")


# Stellaris game Achievements
#url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json"
# Playerdata Koen's account (ReboundQ3)
#url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=3B9518C4F0770B32EC2AB7A6B635E077&steamids=76561198044252418&format=json"
# Featured items
#url = "http://store.steampowered.com/api/featuredcategories/?l=english"


# RocketLeague, TF2, CS:GO, Terraria, Stellaris, BF 2042
gamesToCheck = {
    "RocketLeague" : 252950,
    "TF2" : 440, 
    "CS:GO" : 730,
    "Terria" : 105600,
    "Stellaris" : 281990,
    "BF2042" : 1517290
}


# for game in gamesToCheck:
#     # Number of players
#     print("Current players playing " + game + ": ", end="")
    
#     url = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=" + str(gamesToCheck[game])
#     #url = "https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid=" + str(gamesToCheck[game])
#     response = urlopen(url)
#     # print("===================================================================================================")
#     data_json = json.loads(response.read())
#     #print(data_json)
#     print(data_json['response']['player_count'])

url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?gameid="
response = urlopen(url)
data_json = json.loads(response.read())['applist']['apps']
i = 0
for item in data_json:
    #print(item)
    i += 1
print(i)
