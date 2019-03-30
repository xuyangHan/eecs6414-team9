import json
from shapely.geometry import shape, Point
import requests

# open geojson
with open('static/data/york.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))


# get the center of each polygon and reset other parameters
i = 0
while i < len(data['features']):
    feature = data['features'][i]

    polygon = shape(feature['geometry'])
    cent_lat = polygon.centroid.coords[0][1]
    cent_long = polygon.centroid.coords[0][0]
    # api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' \
    #           + str(cent_lat) + ', ' + str(cent_long) + \
    #           '&destinations=M3J1P3&key=AIzaSyDCd0jbz9KTcTtx3QV-DafS44lsXDBAmHY'
    # response = requests.get(url=api_url)
    # response_data = response.json()
    # distance = response_data['rows'][0]["elements"][0]['distance']['value']
    #
    # if distance > 12000:
    #     data['features'].remove(feature)
    # else:
    #     feature.update({'students': 0})
    #     feature.update({'supermarkets': 0})
    #     feature.update({'fitness': 0})
    #     feature.update({'restaurants': 0})
    #     center = {'lat': cent_lat, 'long': cent_long}
    #     feature.update({'center': center})
    #     i += 1

    feature.update({'students': 0})
    feature.update({'supermarkets': 0})
    feature.update({'fitness': 0})
    feature.update({'restaurants': 0})
    center = {'lat': cent_lat, 'long': cent_long}
    feature.update({'center': center})
    i += 1


# write new json
with open('static/data/york.geojson', 'w') as outfile:
    json.dump(data, outfile)



