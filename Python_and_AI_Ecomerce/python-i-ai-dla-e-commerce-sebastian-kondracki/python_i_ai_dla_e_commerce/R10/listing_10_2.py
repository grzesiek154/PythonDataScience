import urllib.robotparser
import requests
from bs4 import BeautifulSoup

user_agent = "SeKonBot/1.0 (https://zazepa.pl/bot.html)"
url = "https://www.gov.pl/"

rp = urllib.robotparser.RobotFileParser()
rp.set_url(url + "robots.txt")
rp.read()

headers = requests.utils.default_headers()
headers.update({"User-Agent": user_agent})

if rp.can_fetch(user_agent, url+"web/premier/komunikaty-cir"):
    response = requests.get(url+"web/premier/komunikaty-cir",
headers=headers)
    if response.ok:
        page = BeautifulSoup(response.text, 'html.parser')
        elements = page.select('article div.art-prev.art-prev--near-menu ul li div div.title')
        for element in elements:
            print(element.text)
else:
    print("Brak dostępu do CIR KOMUNIKTATY dla robota")