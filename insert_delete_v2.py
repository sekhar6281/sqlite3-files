import sqlite3
import sys
print("Enter the database name:")
database = sys.argv[1]
connection=sqlite3.connect(database)
cursor=connection.cursor()
print('1. Insert records\n2. Delete records')
choice = int(input("Choose the option: "))
if choice == 1:
    id = int(input("Enter the ID: "))
    origin = input("Enter the origin: ")
    destination = input("Enter the destination: ")
    duration = int(input("Enter the duration: "))
    cursor.execute("INSERT INTO flights VALUES (?, ?, ?, ?)", (id, origin, destination, duration))
    connection.commit()
    print("Record inserted successfully.")
    cursor.execute("SELECT * FROM flights")
    print(cursor.fetchall())
elif choice == 2:
    flight_id = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM flights WHERE id=?", (flight_id,))
    connection.commit()
    print(f"Flight {flight_id} deleted successfully.")
    cursor.execute("SELECT * FROM flights")
    print(cursor.fetchall())
else:
    print("Invalid choice.")
connection.close()


