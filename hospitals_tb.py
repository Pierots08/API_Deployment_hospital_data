import folium
from folium.plugins import MarkerCluster
import pandas as pd
import requests

list_health = ["hospital", "clinic", "doctors"]

dataframes = []
for amenity in list_health: 
    overpass_url = "http://overpass-api.de/api/interpreter"

    overpass_query = f"""
    [out:json];
    node["amenity"= {amenity}]
      (40.40, -3.71,40.54, -3.60);
    out;
    """
    # the bridge está en el Latitud: 40.421703 Longitud: -3.691725
    response = requests.get(overpass_url, params={'data': overpass_query})
    try: 
        data = response.json()
        df = json_to_df(data)
        dataframes.append(df)
    except:
        continue

health_csv = pd.concat(dataframes)

coordenadas_TB = (40.421703,-3.691725)


some_map2 = folium.Map(location=coordenadas_TB, zoom_start=14)