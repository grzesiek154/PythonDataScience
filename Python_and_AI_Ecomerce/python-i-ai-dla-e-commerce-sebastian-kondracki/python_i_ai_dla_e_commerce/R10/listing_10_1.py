import urllib.robotparser
import requests
import time

user_agent = "SeKonBot/1.0 (https://zazepa.pl/bot.html)"
url = "https://www.uokik.gov.pl/"

rp = urllib.robotparser.RobotFileParser()
rp.set_url(url + "robots.txt")
rp.read()

headers = requests.utils.default_headers()
headers.update({"User-Agent": user_agent,})

if rp.can_fetch(user_agent, url):
    response = requests.get(url, headers=headers)
    if response.ok:
        print("HOME", response.headers)
else:
    print("Brak dostępu do HOME dla robota")

time.sleep(5)

if rp.can_fetch(user_agent, url + "prawo.php"):
    response = requests.get(url + "prawo.php", headers=headers)
    if response.ok:
        print("PRAWO:", response.headers)
else:
    print("Brak dostępu do HOME dla robota")
