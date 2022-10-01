from elasticsearch import Elasticsearch
import requests

es = Elasticsearch([{"host": "localhost", "port": 9200}])
r = requests.get("https://danepubliczne.imgw.pl/api/data/synop")

if r.ok:
    data = r.json()
    for station_data in data:
        response = es.index(index="pogoda", id=id, body=station_data)
        print(response)