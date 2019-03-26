import json
from shapely.geometry import shape, Point

# open geojson
with open('static/data/map.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))


# get the center of each polygon and reset other parameters
for feature in data['features']:
    feature.update({'students': 0})
    feature.update({'supermarkets': 0})
    feature.update({'fitness': 0})
    feature.update({'restaurants': 0})
    polygon = shape(feature['geometry'])
    cent_lat = polygon.centroid.coords[0][1]
    cent_long = polygon.centroid.coords[0][0]
    center = {'lat': cent_lat, 'long': cent_long}
    feature.update({'center': center})

# write new json
with open('static/data/map.geojson', 'w') as outfile:
    json.dump(data, outfile)



