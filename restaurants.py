import pandas as pd
import requests

# some codes to get supermarkets around york university lat and long from google maps api
api_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restqurant%20around%20york%20university&key=AIzaSyDx5AdpkLfmEeXncr9rjw3j9h6TKpcRGbY'

response = requests.get(url=api_url)
data = response.json()
lat = []
long = []
name = []
rating = []
for d in data['results']:
    loc_lat = d["geometry"]['location']['lat']
    loc_long = d["geometry"]['location']['lng']
    d_name = d['name']
    d_rating = d['rating']
    lat.append(loc_lat)
    long.append(loc_long)
    name.append(d_name)
    rating.append(d_rating)

# some codes to get 20 more supermarkets around york university lat and long from google maps api
new_api_url = api_url + '&pagetoken=' + data['next_page_token']
new_response = requests.get(url=new_api_url)
new_data = new_response.json()

for f in new_data['results']:
    loc_lat = f["geometry"]['location']['lat']
    loc_long = f["geometry"]['location']['lng']
    f_name = f['name']
    f_rating = f['rating']
    lat.append(loc_lat)
    long.append(loc_long)
    name.append(f_name)
    rating.append(f_rating)

# some codes to get 20 more supermarkets around york university lat and long from google maps api
new_new_api_url = new_api_url + '&pagetoken=' + new_data['next_page_token']
new_new_response = requests.get(url=new_api_url)
new_new_data = new_new_response.json()

for g in new_new_data['results']:
    loc_lat = g["geometry"]['location']['lat']
    loc_long = g["geometry"]['location']['lng']
    g_name = g['name']
    g_rating = g['rating']
    lat.append(loc_lat)
    long.append(loc_long)
    name.append(g_name)
    rating.append(g_rating)

# some codes to generate a csv file containing lat, long, name and rating
df = pd.DataFrame(columns=['lat', 'long', 'name', 'rating'])
df['lat'] = lat
df['long'] = long
df['name'] = name
df['rating'] = rating
writer = pd.ExcelWriter('static/data/restaurants.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')
writer.save()
