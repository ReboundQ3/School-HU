#%%
#> Koen's pretty pictures by NASA script.
#> Imports
import urllib3 as url
import urllib3.request as req
import json
import pprint
from urllib.request import urlopen
from PIL import Image

####################################
# NASA API KEY: fHujtbxs0XM9CHFe5YbkvfTQTYn3KL5JapFhaTeU
####################################

API_Link = urlopen("https://api.nasa.gov/planetary/apod?api_key=fHujtbxs0XM9CHFe5YbkvfTQTYn3KL5JapFhaTeU&date=")
API_Link_Response = API_Link.getcode()

if API_Link_Response == 200:
    print("> NASA API OK | Code:", API_Link_Response)
else:
    print("> NASA API ERROR | Code:", API_Link_Response)

API_Link_DATA = json.loads(API_Link.read())
pprint.pprint(API_Link_DATA)

#print("===========================================")
#
#print(API_Link_DATA['hdurl'])
#
#print("===========================================")
#
#for keys, value in API_Link_DATA.items():
#    pprint.pprint(keys)
#    
#print("===========================================")

API_Link_URL = urlopen(API_Link_DATA['hdurl'])
API_Link_Picture = Image.open(API_Link_URL)
API_Link_Picture.show()


# %%
