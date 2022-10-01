import sqlite3
import numpy as np

def get_temperature_by_station_id(sid):
    cursor = connection.cursor()
    sql = "SELECT temperature FROM weather WHERE station_id= ?"
    cursor.execute(sql, (sid,))
    result = cursor.fetchall()
    cursor.close()
    return result

connection = sqlite3.connect("weather.db")
rows = get_temperature_by_station_id(12375)
data = np.array(rows, dtype=np.dtype("float"))
print(np.mean(data))
connection.close()