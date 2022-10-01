import sqlite3

def get_all_records():
    cursor = connection.cursor()
    sql = "SELECT weather.*, station.name FROM weather INNER JOIN station ON weather.station_id=station.id"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

connection = sqlite3.connect("weather.db")
rows = get_all_records()
for row in rows:
    print(row)

connection.close()