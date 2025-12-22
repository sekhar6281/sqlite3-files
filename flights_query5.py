import sqlite3
conn = sqlite3.connect("flights.db" )
cursor = conn.cursor()
cursor.execute("select * from flights where origin='Visakhapatnam'")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
