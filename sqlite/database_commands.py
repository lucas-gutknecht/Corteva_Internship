import sqlite3
import os
import csv

con = sqlite3.connect("weather.db")

cursor = con.cursor()

cursor.execute("DROP TABLE IF EXISTS WEATHER")
cursor.execute("CREATE TABLE WEATHER(date string, max_temp float, min_temp float, percipitation float)")

for file in os.listdir("../data"):
    with open(f"../data/{file}", 'r') as opened_file:
        reader = csv.reader(opened_file, delimiter='\t')
        for line in reader:
            cursor.execute(f"INSERT INTO WEATHER VALUES ({line[0].strip()}, {line[1].strip()}, {line[2].strip()}, {line[3].strip()})")
    
con.commit()
con.close()