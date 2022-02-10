import sqlite3, csv

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS city
              (Country TEXT, City TEXT, CityId INTEGER)''')
              

with open('full_city_list.csv', 'r') as file:  
    for row in file:
        cursor.execute("INSERT INTO city VALUES (?, ?, ?)", row.split(";"))
        connection.commit()
    



records = cursor.execute("SELECT * FROM city")

print(cursor.fetchall())

connection.commit()
connection.close()