import csv
import os
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

user_agent = "SeKonBot/1.0 (https://zazepa.pl/bot.html)"
headers = requests.utils.default_headers()
headers.update({"User-Agent": user_agent,})

base_dir = os.path.dirname(__file__)
html_dir = os.path.join(base_dir, "html")
txt_dir = os.path.join(base_dir, "txt")
csv_file = os.path.join(base_dir, "urls.csv")

os.makedirs(html_dir, exist_ok=True)
os.makedirs(txt_dir, exist_ok=True)

def get_content(url):
    title = urlparse(url).path.replace("/", "")
    path_file_html = os.path.join(html_dir, title + ".html")
    path_file_txt = os.path.join(txt_dir, title + ".txt")
    response = requests.get(url, headers=headers)
    if response.ok:
        html = response.text
        with open(path_file_html, "w") as f:
            f.write(html)
        page = BeautifulSoup(html, "html.parser")
        with open(path_file_txt, "w") as f:
            f.write(page.getText())
    print("Plik {} zapisany pomyślnie!".format(title))

with open(csv_file) as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        get_content(row["url"])