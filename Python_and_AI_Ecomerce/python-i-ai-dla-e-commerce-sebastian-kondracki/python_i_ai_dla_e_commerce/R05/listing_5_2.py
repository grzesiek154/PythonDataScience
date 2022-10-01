import requests
import json
import sqlite3


def exists_weather(station_id, measured_at_date, measured_at_hour):

    measured_at = measured_at_date + " " + str(measured_at_hour).zfill(2) + ":00:00"
    cursor = connection.cursor()
    sql = "SELECT count(*) FROM weather WHERE station_id = ? AND measured_at = ?"

    cursor.execute(
        sql,
        (
            station_id,
            measured_at,
        ),
    )

    result = cursor.fetchone()
    cursor.close()

    return result is not None and result[0] > 0


def exists_station(station_id):
    cursor = connection.cursor()
    sql = "SELECT count(*) FROM station WHERE id = ?"
    cursor.execute(sql, (station_id,))
    result = cursor.fetchone()
    cursor.close()

    return result is not None and result[0] > 0


def add_station(station_id, name):
    cursor = connection.cursor()
    sql = "INSERT INTO station (id, name) VALUES (?, ?)"
    val = (
        station_id,
        name,
    )
    cursor.execute(sql, val)
    connection.commit()
    print(station_id, name)


def add_weather(
    station_id, measured_at_date, measured_at_hour, temperature, pressure, rainfall
):

    measured_at = measured_at_date + " " + str(measured_at_hour).zfill(2) + ":00:00"
    val = (station_id, measured_at, temperature, pressure, rainfall)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO weather (station_id, measured_at, temperature, pressure, rainfall) VALUES (?, ?, ?, ?, ?)",
        val,
    )
    connection.commit()
    cursor.close()


connection = sqlite3.connect("weather.db")
r = requests.get("https://danepubliczne.imgw.pl/api/data/synop")

if r.ok:
    data = r.json()
    for station_data in data:

        if not exists_station(station_data["id_stacji"]):
            add_station(station_data["id_stacji"], station_data["stacja"])
            print("Stacja dodana:", station_data["stacja"])
        else:
            print("Stacja już była dodana:", station_data["stacja"])

        if not exists_weather(
            station_data["id_stacji"],
            station_data["data_pomiaru"],
            station_data["godzina_pomiaru"],
        ):
            add_weather(
                station_data["id_stacji"],
                station_data["data_pomiaru"],
                station_data["godzina_pomiaru"],
                station_data["temperatura"],
                station_data["cisnienie"],
                station_data["suma_opadu"],
            )
            print("Pogoda dla stacji dodana:", station_data["stacja"])
        else:
            print("Pogoda dla stacji już była dodana:", station_data["stacja"])

connection.close()
