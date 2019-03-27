import pandas as pd
import math
import requests

# read all postal codes from scratch yuride file
yuData = pd.read_excel(r'static/data/yuride_postalcodes.xlsx')
                        #sheetname='Sheet1', header=0, converters={'Affiliation':str, 'Postal Code':str})

cPostalCodes = pd.read_csv(r'static/data/canadianpostalcodes.csv')

del cPostalCodes['FSA1']
del cPostalCodes['FSA-Province']
del cPostalCodes['AreaType']

#fsaDict = {'empty': {'empty': 'empty', 'lat': 35}}
#for postalRecord in cPostalCodes.items():
#    if postalRecord['FSA'] in fsaDict:
#        postDict = fsaDict[postalRecord]
#        postDict[cPostalCodes['PostalCode']] = {'place': cPostalCodes['PostalCode'], 'lat':cPostalCodes['Latitude'], 'lon':cPostalCodes['Longitude']}
#    else:
#        fsaDict[postalRecord['FSA']].update({'place': postalRecord['Place Name'], 'lat': postalRecord['Latitude'], 'lon': postalRecord['Longitude']})
#
#print(len(fsaDict))

# example
# myseries[myseries == 7]
# output: 3    7
#         dtype: int64
# myseries[myseries == 7].index[0]
# output: 3

#print(cPostalCodes['PostalCode'][cPostalCodes['PostalCode'] == 'L1X2L6'])
#print( (cPostalCodes['PostalCode'] == 'L2B6A7').any())

#index = cPostalCodes['PostalCode'][cPostalCodes['PostalCode'] == 'L1X2L6'].index[0]
#print(cPostalCodes['Latitude'][index], cPostalCodes['Longitude'][index], index, cPostalCodes['PostalCode'][index])

pCount = 0
emptyCount = 0
procCodes = {'PostalCode': {'Latitude': 0, 'Longitude': 0, 'Count': 0, 'Place Name': 'None'}}
scratchCodes = []
fsaCodes = []
# process each postal codes, filter them for considerable values
for pCode in yuData['Postal Code']:
    if type(pCode) is float:
        if math.isnan(pCode):
            emptyCount = emptyCount + 1
        else:
            scratchCodes.append(pCode)
    elif type(pCode) is int:
        scratchCodes.append(pCode)
    else:
        pCode = pCode.replace(" ", "").replace("-", "").replace(",", "")\
                    .replace("'", "").replace("?", "").upper()

        if len(pCode) == 3:
            fsaCodes.append(pCode)
        elif len(pCode) != 6:
            scratchCodes.append(pCode)
        else:
            pCount = pCount + 1
            if pCode in procCodes:
                procCodes[pCode]['Count'] = procCodes[pCode]['Count'] + 1
            else:
                procCodes[pCode] = {'Latitude': 0, 'Longitude': 0, 'Count': 1, 'Place Name': 'None'}

        # print(postalCode[:3].upper())

pNotFound = 0
for pCode, pDetails in procCodes.items():
    if (cPostalCodes['PostalCode'] == pCode).any():
        index = cPostalCodes['PostalCode'][cPostalCodes['PostalCode'] == pCode].index[0]
        print(pCode, index)
        pDetails['Latitude'] = cPostalCodes['Latitude'][index]
        pDetails['Longitude'] = cPostalCodes['Longitude'][index]
        pDetails['Place Name'] = cPostalCodes['Place Name'][index]
    else:
        pNotFound = pNotFound + 1
        #if pNotFound == 3:
        #    break

writer = pd.ExcelWriter('static/data/yuride_postalcodes_filtered.xlsx', engine='openpyxl')
procCodes = pd.DataFrame(procCodes).T
procCodes.to_excel(writer, sheet_name='Postal Details')

fsaCodes = pd.DataFrame(fsaCodes)
fsaCodes.to_excel(writer, sheet_name='FSA ONLY')

scratchCodes = pd.DataFrame(scratchCodes)
scratchCodes.to_excel(writer, sheet_name='Scratch Sheet')
writer.save()
writer.close()

print(pCount, emptyCount, pCount + emptyCount + len(scratchCodes) + len(fsaCodes), pNotFound)
