#%%
#Steam_Database.py
# Alle imports

import os
from os import path
import sqlite3

# > DB

print("==================================================================")

if path.exists("steamdb.db"):
    print("> STEAM DB ALREADY EXISTS SKIPPING")
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
else:
    print("> STEAM DB CREATED")
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
    DB_CON.execute("CREATE TABLE tbl_games(game_id, game_name)")
    DB_CON.execute("CREATE TABLE tbl_stats(date, game_id, game_name, playercount)")

print("==================================================================")

# RocketLeague, TF2, CS:GO, Terraria, Stellaris, BF 2042
gamesToCheck = {
    "Counter-Strike: Global Offensive" : 730,
    "Dota 2" : 570,
    "Apex Legends" : 1172470,
    "PUBG: BATTLEGROUNDS" : 578080,
    "Grand Theft Auto V" : 271590,
    "Resident Evil 4" : 2050650,
    "Source SDK Base 2007" : 218,
    "Team Fortress 2" : 440,
    "Wallpaper Engine" : 431960,
    "Rust" : 980030,
    "Lost Ark" : 1599340,
    "Destiny 2" : 1085660,
    "Call of Duty: Modern Warfare II  Warzone 2.0" : 1938090,
    "NARAKA: BLADEPOINT" : 1203220,
    "War Thunder" : 236390,
    "Unturned" : 304930,
    "Football Manager 2023" : 1904540,
    "Sid Meier's Civilization VI" : 289070,
    "ARK: Survival Evolved" : 346110,
    "Warframe" : 230410,
    "EA SPORTS FIFA 23" : 1811260,
    "Crab Game" : 1782210,
    "Hogwarts Legacy" : 990080,
    "Tom Clancy's Rainbow Six Siege" : 359550,
    "ELDEN RING" : 1245620,
    "PAYDAY 2" : 218620,
    "Terraria" : 105600,
    "DayZ" : 221100,
    "Hearts of Iron IV" : 394360,
    "Red Dead Redemption 2" : 1174180,
    "Euro Truck Simulator 2" : 227300,
    "Stardew Valley" : 413150,
    "MIR4" : 1623660,
    "Goose Goose Duck" : 1568590,
    "Monster Hunter: World" : 582010,
    "Left 4 Dead 2" : 550,
    "The Sims 4" : 1222670,
    "Total War: WARHAMMER III" : 1142710,
    "Dead by Daylight" : 381210,
    "Summoners War: Chronicles" : 2167580,
    "Don't Starve Together" : 322330,
    "Sons Of The Forest" : 1326470,
    "Cities: Skylines" : 255710,
    "Valheim" : 892970,
    "Project Zomboid" : 108600,
    "Spacewar" : 480,
    "7 Days to Die" : 251570,
    "Farming Simulator 22" : 1248130,
    "NBA 2K23" : 1919590,
    "MONSTER HUNTER RISE" : 1446780,
    "Garry's Mod" : 4000,
    "Stellaris" : 281990,
    "Mount & Blade II: Bannerlord" : 261550,
    "tModLoader" : 1281930,
    "Sea of Thieves" : 1172620,
    "RimWorld" : 294100,
    "The Elder Scrolls V: Skyrim Special Edition" : 489830,
    "The Witcher 3: Wild Hunt" : 292030,
    "Albion Online" : 761890,
    "Cyberpunk 2077" : 1091500,
    "VRChat" : 438100,
    "Deep Rock Galactic" : 548430,
    "Black Desert" : 582660,
    "Age of Empires II: Definitive Edition" : 813780,
    "Europa Universalis IV" : 236850,
    "Satisfactory" : 526870,
    "The Elder Scrolls Online" : 306130,
    "Brotato" : 1942280,
    "Rocket League" : 252950,
    "The Binding of Isaac: Rebirth" : 250900,
    "Sid Meier's Civilization V" : 8930,
    "Fallout 4" : 377160,
    "Slay the Spire" : 646570,
    "Hunt: Showdown" : 594650,
    "FINAL FANTASY XIV Online" : 39210,
    "Sekiro: Shadows Die Twice" : 814380,
    "Forza Horizon 5" : 1551360,
    "Football Manager 2022" : 1569040,
    "Crusader Kings III" : 1158310,
    "Path of Exile" : 238960,
    "Battlefield 2042" : 1517290,
    "Conan Exiles" : 440900,
    "Factorio" : 427520,
    "World of Tanks Blitz" : 444200,
    "Arma 3" : 107410,
    "Soundpad" : 629520,
    "New World" : 1063730,
    "SCUM" : 513710,
    "Oxygen Not Included" : 457140,
    "Battlefield V" : 1238810,
    "Squad" : 393380,
    "Last Epoch" : 899770,
    "FIFA 22" : 1506830,
    "Ori and the Will of the Wisps" : 1057090,
    "BeamNG.drive" : 284160,
    "Counter-Strike" : 10,
    "Cookie Clicker" : 1454400
}

DB_CUR.execute("DELETE FROM tbl_games")
for game in gamesToCheck:
    game_name = game
    game_id = gamesToCheck[game]
    DB_CUR.execute("INSERT INTO tbl_games(game_id, game_name) VALUES (?, ?)",
                (game_id, game_name))
    DB_CON.commit()
    
# %%
