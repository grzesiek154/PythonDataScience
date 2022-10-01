import sqlite3

def create_structure():
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS weather(id INTEGER PRIMARY KEY AUTOINCREMENT, station_id INTEGER, measured_at DATETIME, temperature REAL, pressure REAL, rainfall REAL, FOREIGN KEY (station_id) REFERENCES station (station_id))"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS station(id INTEGER PRIMARY KEY, name VARCHAR(50))"
    )
    connection.commit()
    cursor.close()


connection = sqlite3.connect("weather.db")
create_structure()
connection.close()