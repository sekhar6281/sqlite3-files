import sqlite3
connection = sqlite3.connect("flights.db")
cursor = connection.cursor()
cursor.execute("insert into flights values (8, 'bobbili', 'tuni', 30)")
connection.commit()
connection.close()
