import pandas as pd
import requests

# to get codes df from the postal csv
codes_df = pd.read_excel(r'static/data/example.xlsx')

# some codes to get lat and long from google maps api
i = 0
commute_time = []
for time in codes_df['commute_time']:
    for s in time.split():
        if s.isdigit():
            time_num = int(s)
    commute_time.append(time_num)

    i = i + 1
    print(i)


# some codes to generate a csv file with lat and long
codes_df['commute_time_min'] = commute_time
writer = pd.ExcelWriter('static/data/example.xlsx', engine='xlsxwriter')
codes_df.to_excel(writer, sheet_name='sheet1')
writer.save()
