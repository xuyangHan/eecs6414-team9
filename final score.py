import json
import pandas as pd
from shapely.geometry import shape, Point

final_score = pd.read_csv('static/data/final.CSV')

# open geojson
with open('static/data/york.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))

for feature in data['features']:
    polygon = shape(feature['geometry'])
    for index, row in final_score.iterrows():
        p = Point(row['cent_long'], row['cent_lat'])
        if polygon.contains(p):
            feature.update({'score': row['scores']})

# write new json
with open('static/data/york.geojson', 'w') as outfile:
    json.dump(data, outfile)

