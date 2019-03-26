import json
import pandas as pd
from shapely.geometry import shape, Point

# open the data supermarkets and fitness
sup_data = pd.read_csv('static/data/supermarkets.CSV')
fitness_data = pd.read_csv('static/data/fitness.CSV')


# open geojson
with open('static/data/map.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))


for feature in data['features']:
    polygon = shape(feature['geometry'])
    for index, row in sup_data.iterrows():
        p = Point(row['long'], row['lat'])
        if polygon.contains(p):
            feature.update({'supermarkets': feature['supermarkets'] + row['rating']})

    for index, row in fitness_data.iterrows():
        p = Point(row['long'], row['lat'])
        if polygon.contains(p):
            feature.update({'fitness': feature['fitness'] + row['rating']})


# write new json
with open('static/data/map.geojson', 'w') as outfile:
    json.dump(data, outfile)

