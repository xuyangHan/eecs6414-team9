import requests
import pandas as pd


locations = ['York University', 'Vaughan Corporate', 'Humber Summit', 'Emergy', 'Jane and Finch', 'North York',
             'William Baker', 'Downsview', 'North Park',
             'Winston Park', 'Fishervill', 'Streeles Corners']

appendix = ', Ontario'

lat = []
long = []
name = []
loc = []
rating = []

for location in locations:
    # some codes to get supermarkets around york university lat and long from google maps api
    api_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurant%20around%20' \
              + location \
              + appendix \
              + '&key=AIzaSyDx5AdpkLfmEeXncr9rjw3j9h6TKpcRGbY'
    response = requests.get(url=api_url)
    data = response.json()
    for d in data['results']:
        loc_lat = d["geometry"]['location']['lat']
        loc_long = d["geometry"]['location']['lng']
        d_name = d['name']
        d_rating = d['rating']
        lat.append(loc_lat)
        long.append(loc_long)
        name.append(d_name)
        rating.append(d_rating)
        loc.append(location)


# some codes to generate a csv file containing lat, long, name and rating
df = pd.DataFrame(columns=['lat', 'long', 'name', 'location', 'rating'])
df['lat'] = lat
df['long'] = long
df['name'] = name
df['location'] = loc
df['rating'] = rating
writer = pd.ExcelWriter('static/data/all_restaurants.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')
writer.save()
