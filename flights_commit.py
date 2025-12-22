import sqlite3
import sys
connection=sqlite3.connect("flights.db")
cursor=connection.cursor()
cursor.execute("create table if not exists flights(id,origin,destination,duration)")
if len(sys.argv) != 5:
    print("Usage : python3 flights_commit.py <id> <origin> <destination> <duration>")
    sys.exit(1)
id=int(sys.argv[1])
origin=sys.argv[2]
destination=sys.argv[3]
duration=int(sys.argv[4])
cursor.execute("insert into flights values(?,?,?,?)",(id,origin,destination,duration))
cursor.execute("select *  from flights")
print(cursor.fetchall())
connection.commit()
connection.close()        
