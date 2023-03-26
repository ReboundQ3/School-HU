
vandaag_afgk = "10/10/2022"
for game in gamelist:
    game_id  = game[0]  
    game_name = game[1]
    playercount = "891398" # Ophalen via api
    ql = ''' INSERT INTO tbl_stats(Date,Game_id,Game_name,Playercount)
              VALUES(vandaag_afgk,game_id,game_name,playercount) '''



