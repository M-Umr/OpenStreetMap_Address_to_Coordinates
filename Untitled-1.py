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
print(json.dumps(data, indent=2))

#nom = Nominatim()
#g = nom.geocode('Pakistan')
#print(g.latitude, g.longitude)


#parameters = {
 #   'key' : 'LeqGr1rhuMIHfraijSydK9BxsdNTGF7s',
  #  'location' : '250-A Hidayat Ullah Block, Mustafa Town, Lahore, Pakistan'
#}
#location = 'Lahore, Pakistan'
#response = requests.get('http://www.mapquestapi.com/geocoding/v1/address', params=parameters)

#data = json.loads(response.text)['results']
#print(response.json())

