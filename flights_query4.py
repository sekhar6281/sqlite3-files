import sqlite3
conn = sqlite3.connect("flights.db" )
cursor = conn.cursor()
cursor.execute("select * from flights where id = 3")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
