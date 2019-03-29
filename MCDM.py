import json
import pandas as pd
from shapely.geometry import shape, Point

# open the data supermarkets and fitness
fitness_data = pd.read_csv('static/data/all_unique_fitness.CSV', encoding='windows-1252')
sup_data = pd.read_csv('static/data/all_unique_supermarkets.CSV', encoding='windows-1252')
restaurants_data = pd.read_csv('static/data/all_unique_restaurants.CSV', encoding='windows-1252')

# open geojson
with open('static/data/york.geojson') as json_file:
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

    for index, row in restaurants_data.iterrows():
        p = Point(row['long'], row['lat'])
        if polygon.contains(p):
            feature.update({'restaurants': feature['restaurants'] + row['rating']})


# write new json
with open('static/data/york.geojson', 'w') as outfile:
    json.dump(data, outfile)

