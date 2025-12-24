import sqlite3
import sys

database = sys.argv[1]
print(f'Your database is {database}.')
check = ['flights.db', 'flights_ap.db']

if database in check:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    while True:    
        print('1. Insert records\n2. Delete records\n3. Exit')
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

        elif choice == 3:
            connection.close()
            break
    
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

else:
    print("Invalid database name")
