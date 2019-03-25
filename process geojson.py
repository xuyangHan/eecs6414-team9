import json

with open('static/data/map.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))


for feature in data['features']:
    feature.update({'students': 0})


with open('static/data/map.geojson', 'w') as outfile:
    json.dump(data, outfile)



