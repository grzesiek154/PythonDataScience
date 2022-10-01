from sklearn.datasets import load_files
import os
import requests
from zipfile import ZipFile
base_dir = os.path.dirname(__file__)
url = "http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip"
zip_file = "bbc-fulltext.zip"
container = "bbc"
dataset_dir = os.path.join(base_dir, "datasets")
os.makedirs(dataset_dir, exist_ok=True)
r = requests.get(url, stream=True)

with open(os.path.join(base_dir, zip_file), "wb") as fd:
    for chunk in r.iter_content(chunk_size=512):
        fd.write(chunk)
with ZipFile(os.path.join(base_dir, zip_file), "r") as zip_obj:
    zip_obj.extractall(dataset_dir)

dataset = load_files(os.path.join(dataset_dir, container), encoding="utf-8", decode_error="replace")
print("Liczba plików:", len(dataset.filenames))
print("Liczba etykiet", len(dataset.target_names))