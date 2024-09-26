import sqlite3 as sql
from os import path
import random
import logging

if path.exists("database.db"):
    print("#> ==========================")
    print("#> DB ALREADY EXISTS SKIPPING")
    print("#> ==========================")
    DB_CON = sql.connect("database.db")
    DB_CUR = DB_CON.cursor()
else:
    print("#> ==========================")
    print("#> DB CREATED")
    print("#> ==========================")
    DB_CON = sql.connect("database.db")
    DB_CUR = DB_CON.cursor()
    DB_CON.execute("CREATE TABLE tbl_num(nummers)")
    
for i in range(1000):
    DB_CUR.execute(f"INSERT INTO tbl_num(nummers) VALUES ({random.randint(0, 500)})")
    DB_CON.commit()

highest = DB_CUR.execute("SELECT MAX(nummers) AS highest_num FROM tbl_num")
highest = DB_CUR.fetchone()
highest = int(highest[0])
print("#> Het hoogste nummer is:",highest)

lowest = DB_CUR.execute("SELECT MIN(nummers) AS lowest_num FROM tbl_num")
lowest = DB_CUR.fetchone()
lowest = int(lowest[0])
print("#> Het laagste nummer is:",lowest)

all = DB_CUR.execute("SELECT SUM(nummers) AS all_num FROM tbl_num")
all = DB_CUR.fetchone()
all = int(all[0])
print("#> alles opgeteld is:",all)

avarage = DB_CUR.execute("SELECT AVG(nummers) AS avg_num FROM tbl_num")
avarage = DB_CUR.fetchone()
avarage = int(avarage[0])
print("#> alles opgeteld is:",avarage)

DB_CON.close()

