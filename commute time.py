import pandas as pd
import requests

# to get codes df from the postal csv
codes_df = pd.read_excel(r'static/data/example.xlsx')

# some codes to get lat and long from google maps api
i = 0
yorku_code = 'M3J 1P3'
commute_time = []
for code in codes_df['Codes']:
    api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' \
              + code + \
              '&destinations=M3J1P3&key=AIzaSyDCd0jbz9KTcTtx3QV-DafS44lsXDBAmHY'
    response = requests.get(url=api_url)
    data = response.json()
    time = data['rows'][0]["elements"][0]['duration']['text']
    commute_time.append(time)
    i = i + 1
    print(i)


# some codes to generate a csv file with lat and long
codes_df['commute_time'] = commute_time
writer = pd.ExcelWriter('static/data/example.xlsx', engine='xlsxwriter')
codes_df.to_excel(writer, sheet_name='sheet1')
writer.save()