import requests
from bs4 import BeautifulSoup
      
response = requests.get("https://zazepa.pl/v1/")
if response.ok:
    page = BeautifulSoup(response.text, 'html.parser')
    products = page.select('div.product')
    print("Liczba elementów div z produktem (wersja v1 - statyczna):",
len(products))
response = requests.get("https://zazepa.pl/v2/")
if response.ok:
    page = BeautifulSoup(response.text, 'html.parser')
    products = page.select('div.product')
    print("Liczba elementów div z produktem (wersja v2 - dynamiczna):", len(products))