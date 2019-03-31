import pandas as pd
import math
import re
import requests

def add_to_fsa(fsa):
    if fsa.isalnum():
        if fsa in allFsaCodes:
            allFsaCodes[fsa] = allFsaCodes[fsa] + 1
        else:
            allFsaCodes[fsa] = 1
        return True
    return False

# read all postal codes from scratch YURide file
yuRidePC = pd.read_excel(r'static/data/yuride_postalcodes.xlsx') #sheetname='Sheet1', header=0, converters={'Affiliation':str, 'Postal Code':str})

# read all postal codes from Fusion Tables as reference data
fusionTablePC = pd.read_csv(r'static/data/canadianpostalcodes.csv')
#cPostalCodes = pd.read_excel(r'static/data/canadianpostalcodes.xlsx')

# delete/drop un-necessary columns
del fusionTablePC['FSA1']
del fusionTablePC['FSA-Province']
del fusionTablePC['AreaType']

# variables for filtering postal codes from YURide file
pcCount = 0
emptyCount = 0
uniquePCData = {} #{'PostalCode': {'Latitude': 0, 'Longitude': 0, 'Count': 0, 'Place Name': ''}
filteredPCData = []  #  {'Affiliation': '', 'PostalCode': ''}
detailedPCData = []  #{'PostalCode': '', 'FSA': '', 'Latitude': 0, 'Longitude': 0,'Place Name': '', 'Affiliation': ''}
skippedPC = [] # postalcodes not found in Fusion Table
scrapCodes = [] # scrapcodes like sdfsdfesd
scrappyPC = [] # FSA only
allFsaCodes = {}

# process each postal codes, filter them for considerable data frame
for affiliation, pCode in yuRidePC.values:
#for pCode in yuData['PostalCode']:

    if type(pCode) is float:
        if math.isnan(pCode):
            emptyCount = emptyCount + 1
        else:
            scrapCodes.append(pCode)
    elif type(pCode) is int:
        scrapCodes.append(pCode)
    else:
        pCode = pCode.replace(" ", "").replace("-", "").replace(",", "")\
                    .replace("'", "").replace("?", "").upper()
        #pCode = re.sub(r'\W+', '', pCode)

        if len(pCode) == 3:
            scrappyPC.append(pCode)
            add_to_fsa(pCode)
        elif len(pCode) != 6:
            #add_to_fsa(pCode[:3])
            scrapCodes.append(pCode)
        else:
            pcCount = pcCount + 1
            add_to_fsa(pCode[:3])

            filteredPCData.append({'Affiliation': affiliation, 'PostalCode': pCode})

            if pCode in uniquePCData:
                uniquePCData[pCode]['Count'] = uniquePCData[pCode]['Count'] + 1
            else:
                uniquePCData[pCode] = {'FSA': pCode[:3], 'Latitude': 0, 'Longitude': 0, 'Count': 1, 'Place Name': 'None'}

# add details to unique postal code which appeared X times by filtering original data
for pCode, pDetails in uniquePCData.items():
    if (fusionTablePC['PostalCode'] == pCode).any():
        index = fusionTablePC['PostalCode'][fusionTablePC['PostalCode'] == pCode].index[0]
        print(pCode, index)
        pDetails['Latitude'] = fusionTablePC['Latitude'][index]
        pDetails['Longitude'] = fusionTablePC['Longitude'][index]
        pDetails['Place Name'] = fusionTablePC['Place Name'][index]
    else:
        del uniquePCData[pCode]
        skippedPC.append(pCode)
        ## condition for small subset test ##
        #if len(skippedPC) >= 3:
        #    break

counter = 0
# add details to detailed postal code from filtered original data and populated uniquePostal codes data
for pcData in filteredPCData:
    if pcData['PostalCode'] in uniquePCData:
        counter = counter + 1
        data = uniquePCData[pcData['PostalCode']]
        detailedPCData.append({'PostalCode': pcData['PostalCode'], 'FSA': pcData['PostalCode'][:3],
                               'Latitude': data['Latitude'], 'Longitude': data['Longitude'],
                               'Place Name': data['Place Name'], 'Affiliation': pcData['Affiliation']})

#print(counter, len(uniquePCData))

writer = pd.ExcelWriter('static/data/yuride_postalcodes_filtered.xlsx', engine='openpyxl')
detailedPCData = pd.DataFrame(detailedPCData)
detailedPCData.to_excel(writer, sheet_name='Detailed PC')

uniquePCData = pd.DataFrame(uniquePCData).T
uniquePCData.to_excel(writer, sheet_name='Unique PC')

skippedPC = pd.DataFrame(skippedPC)
skippedPC.to_excel(writer, sheet_name='Missing PC')

allFsaCodes = pd.DataFrame(allFsaCodes, index=[0]).T
allFsaCodes.to_excel(writer, sheet_name='All FSA')

scrappyPC = pd.DataFrame(scrappyPC)
scrappyPC.to_excel(writer, sheet_name='Scrap FSA')

scrapCodes = pd.DataFrame(scrapCodes)
scrapCodes.to_excel(writer, sheet_name='Scrap Sheet')

filteredPCData = pd.DataFrame(filteredPCData)
filteredPCData.to_excel(writer, sheet_name='Filtered YURide Data')

writer.save()
writer.close()

print(pcCount, emptyCount, pcCount + emptyCount + len(scrapCodes) + len(scrappyPC), len(skippedPC), len(allFsaCodes))

