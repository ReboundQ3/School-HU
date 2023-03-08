#%%
import urllib.request as requests
from urllib.request import urlopen
import json

# api key: 3B9518C4F0770B32EC2AB7A6B635E077

#respone_API = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json')
#print(respone_API.status_code)


url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=281990&key=3B9518C4F0770B32EC2AB7A6B635E077&steamid=76561198044252418&format=json"

response = urlopen(url)

data_json = json.loads(response.read())

print(data_json)
# %%
