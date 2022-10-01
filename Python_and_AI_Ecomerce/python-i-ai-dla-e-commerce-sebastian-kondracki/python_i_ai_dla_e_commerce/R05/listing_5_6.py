from functools import partial
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="example")
geocode = partial(geolocator.geocode, language="pl")
location = geocode("Nadarzyn")
print(location.address)
print(location.latitude, location.longitude)