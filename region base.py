import json
import pandas as pd
from shapely.geometry import shape, Point
import xlsxwriter

# open geojson
with open('static/data/york.geojson') as json_file:
    data = json.load(json_file)
    print(len(data['features']))


name = []
cent_lat = []
cent_long = []
num_students = []
supermarkets = []
fitness = []
commute_time = []
restaurants = []
score = []

i = 1
for feature in data['features']:
    name.append("R_" + str(i))
    i = i + 1
    cent_long.append(feature['center']['long'])
    cent_lat.append(feature['center']['lat'])
    num_students.append(feature['students'])
    commute_time.append(feature['commute_time'])
    supermarkets.append(feature['supermarkets'])
    fitness.append(feature['fitness'])
    restaurants.append(feature['restaurants'])
    score.append(feature['score'])


# some codes to generate a csv file containing lat, long, name and rating
df = pd.DataFrame(columns=['name', 'cent_lat', 'cent_long', 'num_students',
                           'commute_time', 'supermarkets', 'fitness', 'restaurants', 'score'])
df['name'] = name
df['cent_lat'] = cent_lat
df['cent_long'] = cent_long
df['num_students'] = num_students
df['commute_time'] = commute_time
df['supermarkets'] = supermarkets
df['fitness'] = fitness
df['restaurants'] = restaurants
df['score'] = score

writer = pd.ExcelWriter('static/data/new_york.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')
writer.save()

