import pandas as pd
import requests

# to get codes df from the postal csv
codes_df = pd.read_excel(r'static/data/distribution.xlsx')

# some codes to get lat and long from google maps api
i = 0
lat = []
long = []
for code in codes_df['Codes']:
    api_url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' \
              + code + \
              '&key=AIzaSyDCd0jbz9KTcTtx3QV-DafS44lsXDBAmHY'
    response = requests.get(url=api_url)
    data = response.json()
    loc_lat = data['results'][0]["geometry"]['location']['lat']
    loc_long = data['results'][0]["geometry"]['location']['lng']
    lat.append(loc_lat)
    long.append(loc_long)
    i = i + 1
    print(i)


# some codes to generate a csv file with lat and long
codes_df['lat'] = lat
codes_df['long'] = long
writer = pd.ExcelWriter('static/data/distribution.xlsx', engine='xlsxwriter')
codes_df.to_excel(writer, sheet_name='sheet1')
writer.save()
