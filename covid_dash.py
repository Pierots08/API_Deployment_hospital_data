import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import requests
from datetime import datetime
#https://towardsdatascience.com/building-a-real-time-dashboard-us
ing-python-plotly-library-and-web-service-145f50d204f0
raw=
requests.get("https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgi
s/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query
?where=1%3D1&outFields=*&outSR=4326&f=json")
raw_json = raw.json()
df = pd.DataFrame(raw_json["features"])
data_list = df["attributes"].tolist()
df_final = pd.DataFrame(data_list)
df_final.set_index("OBJECTID")
df_final = df_final[["Country_Region", "Province_State", "Lat",
"Long_", "Confirmed", "Deaths", "Recovered", "Last_Update"]]