#%%
#> Koen's pretty pictures by NASA script.

#> Imports
import urllib3 as url
import urllib3.request as req
import json
import pprint
import sqlite3
import os
from os import path
from urllib.request import urlopen
from PIL import Image

####################################
# NASA API KEY: fHujtbxs0XM9CHFe5YbkvfTQTYn3KL5JapFhaTeU
####################################

#> DB

print("==================================================================")

if path.exists("nasatest.db"):
    print("> NASA DB ALREADY EXISTS SKIPPING")
    DB_CON = sqlite3.connect("nasatest.db")
    CUR = DB_CON.cursor()
else:
    print("> NASA DB CREATED")
    DB_CON = sqlite3.connect("nasatest.db")
    DB_CON.cursor()
    DB_CON.execute("CREATE TABLE data(date, title, explaination, url)")

print("==================================================================")

#> NASA DATA

API_Link = urlopen("https://api.nasa.gov/planetary/apod?api_key=fHujtbxs0XM9CHFe5YbkvfTQTYn3KL5JapFhaTeU&date=")
API_Link_Response = API_Link.getcode()

if API_Link_Response == 200:
    print("> NASA API OK | Code:", API_Link_Response)
    print("==================================================================")
else:
    print("> NASA API ERROR | Code:", API_Link_Response)
    print("==================================================================")

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

print("==================================================================")

DB_DATA_TITLE = API_Link_DATA['title']
DB_DATA_DATE = API_Link_DATA['date']
DB_DATA_URL = API_Link_DATA['url']
DB_DATA_DESC = API_Link_DATA['explanation']

print("> Date:",DB_DATA_DATE)
print("> Title:",DB_DATA_TITLE)
print("> Description:",DB_DATA_DESC)
print("> URL:",DB_DATA_URL)

print("==================================================================")

#> Data -> DB

get = CUR.execute("SELECT * FROM data")
get.fetchall()

def import_data():
    CUR.execute("INSERT INTO data VALUES(?, ?, ?, ?)",
        (DB_DATA_DATE, DB_DATA_TITLE, DB_DATA_DESC, DB_DATA_URL))
    DB_CON.commit()

#> Image laten zien

# API_Link_URL = urlopen(API_Link_DATA['hdurl'])
# API_Link_Picture = Image.open(API_Link_URL)
# API_Link_Picture.show()


# %%
