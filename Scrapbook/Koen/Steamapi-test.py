#%%
import urllib.request as requests
from urllib.request import urlopen
import json
import pprint

# api key: 3B9518C4F0770B32EC2AB7A6B635E077

#respone_API = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json')
#print(respone_API.status_code)

#Stellaris game Achievements
#url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json"
#Playerdata Koen's account (ReboundQ3)
url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=3B9518C4F0770B32EC2AB7A6B635E077&steamids=76561198044252418&format=json"

response = urlopen(url)

data_json = json.loads(response.read())

print(data_json)

print("===================================================================================================")

#x = data_json['personaname']
#print(x)
    
#print("Type:", type(data_json))
#print("\nSteamdata", data_json['personaname'])

pprint.pprint(data_json)
print("===================================================================================================")
pprint.pprint(data_json['response']['players'][0]['personaname'])
# print(data_json[response])

#SQLLITE GEBRUKEN ?
    

# %%
