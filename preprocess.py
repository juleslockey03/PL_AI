import sqlite3
import csv

with open('data/england-premier-league-teams-2018-to-2019-stats.csv') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)


#conn = sqlite3.connect('data/england-premier-league-teams-2018-to-2019-stats.csv')
