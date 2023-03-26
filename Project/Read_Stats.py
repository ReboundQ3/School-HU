# Import modules
import sqlite3
from os import path
import PySimpleGUI as sg
import matplotlib.pyplot as plt

# Check if SQLite DB exist and connect to it
try:    
    DB_CON = sqlite3.connect("steamdb.db")
    DB_CUR = DB_CON.cursor()
    print("> STEAM DB CONNECTED")
except:
    print("> STEAM DB DOES NOT EXIST")

games_list = list(DB_CUR.execute("SELECT game_id, game_name from tbl_games"))
games = []
for game in games_list:
    games.append(game[1])


layout = [[sg.Text("For what game do you want to get the stats?")],
          [sg.Combo(games, enable_events=True, key='_COMBO_')],
          [sg.Button("OK")]]

window = sg.Window("Select game", layout, finalize=True)
comboBox = window['_COMBO_']

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

    elif event == '_COMBO_':
        selection = values[event]
        if selection:
            selectedGame = selection          

stats = list(DB_CUR.execute("SELECT * from tbl_stats WHERE game_name='" + selectedGame + "'"))

dates = []
players = []
for stat in stats:
    dates.append(stat[0])
    players.append(stat[3])

plt.plot(dates, players)
plt.show()
