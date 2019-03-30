import json
import pandas as pd
from shapely.geometry import shape, Point

all_points = pd.read_csv('static/data/mid.CSV')

# open geojson
with open('static/data/york.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))

# Count = []
# Latitude = []
# Longitude = []
# Place_Name = []

i = 0
for feature in data['features']:
    polygon = shape(feature['geometry'])
    for index, row in all_points.iterrows():
        print(i)
        i += 1
        p = Point(row['Longitude'], row['Latitude'])
        if polygon.contains(p):
            # Count.append(row['Count'])
            # Latitude.append(row['Latitude'])
            # Longitude.append(row['Longitude'])
            # Place_Name.append(row['Place Name'])
            feature.update({'students': feature['students'] + row['Count']})

# # some codes to generate a csv file containing lat, long, name and rating
# df = pd.DataFrame(columns=['Count', 'Latitude', 'Longitude', 'Place Name'])
# df['Count'] = Count
# df['Latitude'] = Latitude
# df['Longitude'] = Longitude
# df['Place_Name'] = Place_Name

# writer = pd.ExcelWriter('static/data/mid.xlsx', engine='xlsxwriter')
# df.to_excel(writer, sheet_name='sheet1')
# writer.save()

# write new json
with open('static/data/york.geojson', 'w') as outfile:
    json.dump(data, outfile)


