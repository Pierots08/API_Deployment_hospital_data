import folium
from folium.plugins import MarkerCluster
import pandas as pd
import requests

def json_to_df(data):
    elements = data['elements']
    places = {'category': [], 'lat': [], 'lon': [], 'name': [], 'address': []}
    
    for i in elements:
        
        tipo = i.get('tags', None).get('amenity', None)
        latitude = i.get('lat', None)
        longitude = i.get('lon', None)
        name = i.get('tags', {}).get('name', "NO NAME")
        street = i.get('tags', {}).get('addr:street', "NO STREET")
        number = i.get('tags', {}).get('addr:housenumber', 9999)

        places['category'].append(tipo)
        places['lat'].append(latitude)
        places['lon'].append(longitude)
        places['name'].append(name)
        places['address'].append(street + ' ' + str(number))

            
    return pd.DataFrame(places)