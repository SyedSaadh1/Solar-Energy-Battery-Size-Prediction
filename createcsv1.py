import sys
import csv
import os

import sqlite3
con = sqlite3.connect('battery1')

cur = con.cursor()
cur.execute('SELECT * FROM load;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('load1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('load1.csv file successfully created')
cur.execute('SELECT * FROM energy;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('energy1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('energy1.csv file successfully created')
con.commit()

