import pandas as pd
import requests
import json
from shapely.geometry import shape, Point

# open geojson
with open('static/data/map.geojson') as json_file:
    geo_data = json.load(json_file)
    print(len(geo_data['features']))


# some codes to get lat and long from google maps api
i = 0
for feature in geo_data['features']:
    lat = feature['center']['lat']
    long = feature['center']['long']
    api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' \
              + str(lat) + ', ' + str(long) + \
              '&destinations=M3J1P3&key=AIzaSyDCd0jbz9KTcTtx3QV-DafS44lsXDBAmHY'
    response = requests.get(url=api_url)
    data = response.json()
    time = data['rows'][0]["elements"][0]['duration']['value']
    distance = data['rows'][0]["elements"][0]['distance']['value']

    feature.update({'distance': distance})
    if distance > 3000:
        feature.update({'commute_time': time + 300})
    else:
        feature.update({'commute_time': time})
    i = i + 1
    print(i)


# write new json
with open('static/data/map.geojson', 'w') as outfile:
    json.dump(geo_data, outfile)


