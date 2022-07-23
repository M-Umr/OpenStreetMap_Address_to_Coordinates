from textwrap import indent
import requests
import json
from geopy.geocoders import Nominatim

address = 'HidayatUllah Block Mustafa Town, Lahore'
base_url = 'https://nominatim.openstreetmap.org/search?'
params = {
    'q' : address,
    'format' : 'geocodejson'
}

r = requests.get(base_url, params=params)
#print()
data = json.loads(r.text)
data = json.dumps(data, indent=3)
print(data[1024:]) # Showing the coordinates of the given query
geocod = json.loads(data) #converting String data to Dictionary
print(geocod['geocoding']) #Geocoding, showing the address given to the API