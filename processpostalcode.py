import pandas as pd
import math
import re
import requests

"""
def add_to_fsa(fsa):
    if fsa.isalnum():
        fsaCodes[fsa] = fsaCodes[fsa] + 1
        return True
    return False
"""

# read all postal codes from scratch YURide file
yuData = pd.read_excel(r'static/data/yuride_postalcodes.xlsx') #sheetname='Sheet1', header=0, converters={'Affiliation':str, 'Postal Code':str})

# read all postal codes from Fusion Tables as reference data
cPostalCodes = pd.read_csv(r'static/data/canadianpostalcodes.csv')
#cPostalCodes = pd.read_excel(r'static/data/canadianpostalcodes.xlsx')

# delete/drop un-necessary columns
del cPostalCodes['FSA1']
del cPostalCodes['FSA-Province']
del cPostalCodes['AreaType']

# variables for filtering postal codes from YURide file
pCount = 0
emptyCount = 0
procCodes = {'PostalCode': {'Latitude': 0, 'Longitude': 0, 'Count': 0, 'Place Name': 'None'}}
pCodesNotFound = []
scratchCodes = []
fsaCodes = []

# process each postal codes, filter them for considerable data frame
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
        #pCode = re.sub(r'\W+', '', pCode)

        if len(pCode) == 3:
            fsaCodes.append(pCode)
        elif len(pCode) != 6:
            #add_to_fsa(pCode[:3])
            scratchCodes.append(pCode)
        else:
            pCount = pCount + 1
            #add_to_fsa(pCode[:3])
            if pCode in procCodes:
                procCodes[pCode]['Count'] = procCodes[pCode]['Count'] + 1
            else:
                procCodes[pCode] = {'Latitude': 0, 'Longitude': 0, 'Count': 1, 'Place Name': 'None'}

# add details to unique postal code which appeared X times by filtering original data
for pCode, pDetails in procCodes.items():
    if (cPostalCodes['PostalCode'] == pCode).any():
        index = cPostalCodes['PostalCode'][cPostalCodes['PostalCode'] == pCode].index[0]
        print(pCode, index)
        pDetails['Latitude'] = cPostalCodes['Latitude'][index]
        pDetails['Longitude'] = cPostalCodes['Longitude'][index]
        pDetails['Place Name'] = cPostalCodes['Place Name'][index]
    else:
        del procCodes[pCode]
        pCodesNotFound.append(pCode)
        ## condition for small subset test ##
        #if len(pCodesNotFound) >= 3:
        #    break

writer = pd.ExcelWriter('static/data/yuride_postalcodes_filtered.xlsx', engine='openpyxl')
procCodes = pd.DataFrame(procCodes).T
procCodes.to_excel(writer, sheet_name='Postal Details')

pCodesNotFound = pd.DataFrame(pCodesNotFound)
pCodesNotFound.to_excel(writer, sheet_name='Postal Details Not Found')

fsaCodes = pd.DataFrame(fsaCodes)
fsaCodes.to_excel(writer, sheet_name='FSA ONLY')

scratchCodes = pd.DataFrame(scratchCodes)
scratchCodes.to_excel(writer, sheet_name='Scratch Sheet')
writer.save()
writer.close()

print(pCount, emptyCount, pCount + emptyCount + len(scratchCodes) + len(fsaCodes), len(pCodesNotFound))

