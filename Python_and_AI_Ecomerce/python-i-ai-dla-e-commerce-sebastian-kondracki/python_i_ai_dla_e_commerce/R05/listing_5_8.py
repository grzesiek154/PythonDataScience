from elasticsearch import Elasticsearch
import requests
from functools import partial
from geopy.geocoders import Nominatim
from datetime import datetime

es = Elasticsearch([{"host": "localhost", "port": 9200}])
geolocator = Nominatim(user_agent="example")
geocode = partial(geolocator.geocode, language="pl")
mapping = {
    "mappings": {
        "properties": {
            "location": {"type": "geo_point"},
            "temperature": {"type": "float"},
            "pressure": {"type": "float"},
            "rainfall": {"type": "float"},
        }
    }
}

response = es.indices.create(index="weather", body=mapping, ignore=400)
print(response)
r = requests.get("https://danepubliczne.imgw.pl/api/data/synop")
if r.ok:
    data = r.json()
    for station_data in data:
        location = geocode(station_data["stacja"])
        dt = datetime.fromisoformat(
            station_data["data_pomiaru"]
            + " "
            + str(station_data["godzina_pomiaru"]).zfill(2)
            + ":00:00"
        )
        id = (
            station_data["id_stacji"]
            + "-"
            + station_data["data_pomiaru"]
            + "-"
            + str(station_data["godzina_pomiaru"]).zfill(2)
        )

        doc = {
            "station": station_data["stacja"],
            "measuered_at": dt,
            "temperature": station_data["temperatura"],
            "pressure": station_data["cisnienie"],
            "rainfall": station_data["suma_opadu"],
            "location": {"lat": location.latitude, "lon": location.longitude},
        }
        response = es.index(index="weather", id=id, body=doc)
        print(response)
