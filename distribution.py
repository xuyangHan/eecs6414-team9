import json
import pandas as pd
from shapely.geometry import shape, Point

# open the students data
students_data = pd.read_csv('static/data/Sample Distribution.CSV')


# open geojson
with open('static/data/map.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))


for feature in data['features']:
    polygon = shape(feature['geometry'])
    for index, row in students_data.iterrows():
        p = Point(row['long'], row['lat'])
        if polygon.contains(p):
            feature.update({'students': feature['students'] + row['num']})


# write new json
with open('static/data/map.geojson', 'w') as outfile:
    json.dump(data, outfile)

