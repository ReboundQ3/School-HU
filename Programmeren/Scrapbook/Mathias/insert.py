import urllib as url
import urllib.request
from urllib.request import urlopen
import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import csv

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
newdata = {}
for data in data_json:
    value = data['appid']
    index = data['name']
    newdata[index] = value
#print (newdata)

# print (newdata["Rust"])
games = []
with open(".\Scrapbook\Mathias\Top100games.csv") as csvfile:
    spamreader = csv.reader (csvfile,delimiter=',')
    for row in spamreader:
        print('"' + str(row[0]) + '"',end="")
        print(" : ",end="")
        try: 
            print(newdata[str(row[0])],end=",\n")
        except:
            print("not found")