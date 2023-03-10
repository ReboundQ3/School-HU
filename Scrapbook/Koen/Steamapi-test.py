#%%
# Steamapi-test.py V1.1
#
# STEAM API -> Json TEST
#
# Aan te raden om met Jypyter te runnen want dan print hij wat beter

import urllib as url
import urllib.request
from urllib.request import urlopen
import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# api key: 3B9518C4F0770B32EC2AB7A6B635E077

# API RESPONSE CHECKER 200 == OK
respone_API = urlopen('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json')
#print(respone_API.getcode())
respone_API_code = respone_API.getcode()

if respone_API_code == 200:
    print("> STEAM API OK")
else:
    print("> STEAM API ERROR")


#Stellaris game Achievements
#url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json"
#Playerdata Koen's account (ReboundQ3)
url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=3B9518C4F0770B32EC2AB7A6B635E077&steamids=76561198044252418&format=json"

response = urlopen(url)

data_json = json.loads(response.read())

print("===================================================================================================")

#JSON DATA STAGE 1 | print gwn de gehele dict
print(data_json)

print("===================================================================================================")

#JSON DATA STAGE 2 | print de hele dict in pretty print
pprint.pprint(data_json)
print("===================================================================================================")

#JSON DATA STAGE 3 | Print de steam naam van de player uit de dict in terminal
pprint.pprint(data_json['response']['players'][0]['personaname'])
print("===================================================================================================")

#JSON DATA STAGE 4 | Opent plaatje van steamavatar in default fotobewerker
steam_avatar_URL_GET = data_json['response']['players'][0]['avatarfull']
steam_avatar_URL_OPEN = urlopen(steam_avatar_URL_GET)
steam_avatar_URL_JPG = Image.open(steam_avatar_URL_OPEN)
#steam_avatar_URL_JPG.show()

#JSON DATA STAGE 5 | Opent plaatje in terminal \o/ door middel van het downloaden van JPG en ruimt hem weer op
urllib.request.urlretrieve(steam_avatar_URL_GET, "avatar.jpg")
steam_avatar_URL_PIC = np.asarray(Image.open("avatar.jpg"))
# pprint.pprint(repr(steam_avatar_URL_PIC))
steam_avatar_URL_SHOW = plt.imshow(steam_avatar_URL_PIC)
os.remove("avatar.jpg")

# print(data_json[response])

#SQLLITE GEBRUKEN ?
#Thuis test 2
#Koen Git credentials z6ugwyvaic3wp5ujr3ftullejjc3hs4aggdade3qrge32p2jhhpa
#Koen Token pybu6qltnuke3dxkbsd5m2thxzvqi2q6eal3flmmhigk3dse2b4q
    

# %%
