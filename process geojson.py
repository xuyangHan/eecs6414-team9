import json
import random

with open('static/data/map.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))


for feature in data['features']:
    feature.update({'students': random.randint(1, 101)})


with open('static/data/map.geojson', 'w') as outfile:
    json.dump(data, outfile)



