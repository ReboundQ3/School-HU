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


allGameURL = "https://api.steampowered.com/ISteamApps/GetAppList/v2/?gameid="
response = urlopen(allGameURL)
data_json = json.loads(response.read())['applist']['apps']
i = 0
collector = {}
for item in data_json:
    try:
        gameStatURL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=" + str(item['appid'])
        response = urlopen(gameStatURL)
        data_json = json.loads(response.read())['response']['player_count']
        
        collector[item['appid']] = data_json
        
    except:
        #print("No data found")
        i += 1
    

print(i)
print(collector)