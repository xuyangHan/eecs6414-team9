import pandas as pd

# open the final data
data = pd.read_csv('static/data/final.CSV')

scores = []
for index, row in data.iterrows():
    score = 0.5565 * (1600 - row['commute_time']) / 1000 + 0.2001 * row['supermarkets'] / 100 + 0.1417 * row['fitness'] / 80 \
            + 0.1018 * row['restaurants'] / 150
    scores.append(score)

data['scores'] = scores
writer = pd.ExcelWriter('static/data/final.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name='sheet1')
writer.save()

