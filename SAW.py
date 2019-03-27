import pandas as pd

# open the final data
data = pd.read_csv('static/data/final.CSV')

scores = []
for index, row in data.iterrows():
    score = 0.5 * row['commute_time'] / 1000 + 0.2 * row['supermarkets'] / 15 + 0.15 * row['fitness'] / 30 \
            + 0.05 * row['restaurants']
    scores.append(score)

data['scores'] = scores
writer = pd.ExcelWriter('static/data/final.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name='sheet1')
writer.save()

