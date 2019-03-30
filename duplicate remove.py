import pandas as pd

# read all postal codes from scratch YURide file
data = pd.read_excel(r'static/data/all_restaurants.xlsx')

idx = []
lat = []
long = []
name = []
loc = []
rating = []


i = 0
for index, row in data.iterrows():
    if row['lat'] not in lat:
        lat.append(row['lat'])
        idx.append(i)
    i += 1


i = 0
for index, row in data.iterrows():
    if i in idx:
        long.append(row['long'])
        name.append(row['name'])
        rating.append(row['rating'])
        loc.append(row['location'])
    i += 1


# some codes to generate a csv file containing lat, long, name and rating
df = pd.DataFrame(columns=['lat', 'long', 'name', 'location', 'rating'])
df['lat'] = lat
df['long'] = long
df['name'] = name
df['location'] = loc
df['rating'] = rating
writer = pd.ExcelWriter('static/data/all_unique_restaurants.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')
writer.save()

