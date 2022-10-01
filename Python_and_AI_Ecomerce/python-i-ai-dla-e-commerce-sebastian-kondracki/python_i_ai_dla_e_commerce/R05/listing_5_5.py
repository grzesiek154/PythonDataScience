import sqlite3

def get_avg_temperature_by_station_id(sid):
    cursor = connection.cursor()
    sql = "SELECT AVG(temperature) FROM weather WHERE station_id= ?"
    cursor.execute(sql, (sid,))
    result = cursor.fetchone()[0]
    cursor.close()
    return result

connection = sqlite3.connect("weather.db")
mean = get_avg_temperature_by_station_id(12375)
print(mean)
connection.close()