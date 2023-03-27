# Import modules
import sqlite3
from os import path
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import paramiko
from scp import SCPClient


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient("20.8.110.244", 22, "root", "ML48%u$cfkp2xSGeqHZnxG^Y3")
scp = SCPClient(ssh.get_transport())

scp.get('/project/steamdb.db')

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

plt.figure(figsize=(25,13))
plt.plot(dates,players)
plt.show()
