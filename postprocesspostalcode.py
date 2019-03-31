import pandas as pd

# UNIQUE FSA for GTA region from Unique PC sheet

uniqueFSA = pd.read_excel(open('static/data/yuride_postalcodes_filtered-master.xlsx', 'rb'),
                                sheetname='Unique PC') #replace with Unique PC and update uniqueFSA.values in loop

#gtaplaceNames = ['Bowmanville','Hampton','Seagrave','Udora','Cannington','Pefferlaw','Sutton West','Beeton','Bond Head',
#                 'Holland Landing','Nobleton','Schomberg','East Gwillimbury','New Tecumseth','Brougham','Gormley',
#                 'Greenwood','Kleinburg','Campbellville','Moffat','Halton Hills','Courtice','Oshawa','Whitby','Ajax',
#                 'Pickering','Claremont','Markham','Unionville','Richmond Hill','Thornhill','Newmarket','Stouffville',
#                 'Whitchurch-Stouffville','Aurora','Woodbridge','Vaughan','Concord','Mississauga','Meadowvale','Maple',
#                 'Scarborough','Oakville','Brampton','Springbrook','King City','King','Caledon','Caledon East','Cheltenham',
#                 'Inglewood','Bolton','Georgetown','Acton','Alton','Caledon Village','Burlington','Hamilton','Stoney Creek',
#                 'Ancaster','Dundas','Port Perry','River Drive Park','Uxbridge','Milton','Toronto','North York','North Bay',
#                 'York','East York','Etobicoke']

uniqueFSAList = {}
for postalcode, count, fsa, lat, lng, place in uniqueFSA.values:
    #if place in gtaplaceNames:
    if fsa in uniqueFSAList:
        uniqueFSAList[fsa]['Count'] = uniqueFSAList[fsa]['Count'] + count
    else:
        uniqueFSAList[fsa] = {'Count': count, 'Place Name': place}

writer = pd.ExcelWriter('static/data/yuride_postalcodes_filtered-uniquefsa.xlsx', engine='openpyxl')

uniqueFSAList = pd.DataFrame(uniqueFSAList).T
uniqueFSAList.to_excel(writer, sheet_name='Unique FSA')

writer.save()
writer.close()

print(len(uniqueFSAList))


# affiliation based filtering for GTA region
'''
affiliationPC = pd.read_excel(open('static/data/yuride_postalcodes_filtered-master.xlsx', 'rb'),
                                sheetname='Student PC') #change sheetname for respective affialation sheet name

# OLD FSA
#gtafsa = ['L0G','L0P','L1G','L1H','L1J','L1K','L1L','L1M','L1N','L1P','L1R','L1S','L1T','L1V','L1W','L1X','L1Y','L1Z',
#          'L3P','L3R','L3S','L3T','L3X','L3Y','L4A','L4B','L4C','L4E','L4G','L4H','L4J','L4S','L4T','L4V','L4W','L4X',
#          'L4Y','L4Z','L5A','L5B','L5C','L5E','L5G','L5H','L5J','L5K','L5L','L5M','L5N','L5R','L5S','L5V','L5W','L6A',
#          'L6B','L6C','L6E','L6G','L6H','L6J','L6K','L6L','L6M','L6P','L6R','L6S','L6T','L6V','L6W','L6X','L6Y','L6Z',
#          'L7A','L7B','L7C','L7E','L7K','L7L','L7M','L7N','L7P','L7R','L7S','L7T','L9P','L9T','M1B','M1H','M1L','M1P',
#          'M1T','M1V','M1W','M2N','M2P','M3C','M3J','M4C','M4E','M4J','M4K','M4L','M4M','M4N','M4P','M4R','M4S','M4T',
#          'M4V','M4W','M4X','M4Y','M5A','M5B','M5C','M5E','M5G','M5H','M5J','M5M','M5N','M5P','M5R','M5S','M5T','M5V',
#          'M6B','M6C','M6E','M6G','M6H','M6J','M6K','M6N','M6P','M6R','M6S','M9M','M9P','M9R','M9V','M9W']

detailedPCData = [] #{'PostalCode': '', 'FSA': '', 'Latitude': 0, 'Longitude': 0,'Place Name': '', 'Affiliation': ''}

for aff, fsa, lat, lng, place, postalcode in affiliationPC.values:
    if fsa in gtafsa:
        detailedPCData.append({'PostalCode': postalcode, 'FSA': fsa,
                               'Latitude': lat, 'Longitude': lng,
                               'Place Name': place, 'Affiliation': aff})

writer = pd.ExcelWriter('static/data/yuride_postalcodes_gtacommunity.xlsx', engine='openpyxl')
detailedPCData = pd.DataFrame(detailedPCData)
detailedPCData.to_excel(writer, sheet_name='GTA Community PC')

writer.save()
writer.close()

print(len(detailedPCData))
'''

''''
# unique postal code filtering for GTA
uniquePC = pd.read_excel(open('static/data/yuride_postalcodes_filtered-master.xlsx', 'rb'),
                                sheetname='Unique PC')

#OLD
#gtafsa = ['L0G','L0P','L1G','L1H','L1J','L1K','L1L','L1M','L1N','L1P','L1R','L1S','L1T','L1V','L1W','L1X','L1Y','L1Z',
#          'L3P','L3R','L3S','L3T','L3X','L3Y','L4A','L4B','L4C','L4E','L4G','L4H','L4J','L4S','L4T','L4V','L4W','L4X',
#          'L4Y','L4Z','L5A','L5B','L5C','L5E','L5G','L5H','L5J','L5K','L5L','L5M','L5N','L5R','L5S','L5V','L5W','L6A',
#          'L6B','L6C','L6E','L6G','L6H','L6J','L6K','L6L','L6M','L6P','L6R','L6S','L6T','L6V','L6W','L6X','L6Y','L6Z',
#          'L7A','L7B','L7C','L7E','L7K','L7L','L7M','L7N','L7P','L7R','L7S','L7T','L9P','L9T','M1B','M1H','M1L','M1P',
#          'M1T','M1V','M1W','M2N','M2P','M3C','M3J','M4C','M4E','M4J','M4K','M4L','M4M','M4N','M4P','M4R','M4S','M4T',
#          'M4V','M4W','M4X','M4Y','M5A','M5B','M5C','M5E','M5G','M5H','M5J','M5M','M5N','M5P','M5R','M5S','M5T','M5V',
#          'M6B','M6C','M6E','M6G','M6H','M6J','M6K','M6N','M6P','M6R','M6S','M9M','M9P','M9R','M9V','M9W']


gtafsa = ['M1B','M1C','M1E','M1G','M1H','M1J','M1K','M1L','M1M','M1N','M1P','M1R','M1S','M1T','M1V','M1W','M1X','M2H',
          'M2J','M2K','M2L','M2M','M2N','M2P','M2R','M3A','M3B','M3C','M3H','M3J','M3K','M3L','M3M','M3N','M4A','M4B',
          'M4C','M4E','M4G','M4H','M4J','M4K','M4L','M4M','M4N','M4P','M4R','M4S','M4T','M4V','M4W','M4X','M4Y','M5A',
          'M5B','M5C','M5E','M5G','M5H','M5J','M5K','M5L','M5M','M5N','M5P','M5R','M5S','M5T','M5V','M5W','M5X','M6A',
          'M6B','M6C','M6E','M6G','M6H','M6J','M6K','M6L','M6M','M6N','M6P','M6R','M6S','M7A','M7R','M7Y','M8V','M8W',
          'M8X','M8Y','M8Z','M9A','M9B','M9C','M9L','M9M','M9N','M9P','M9R','M9V','M9W','L1B','L1C','L1E','L1G','L1H',
          'L1J','L1K','L1L','L1M','L1N','L1P','L1R','L1S','L1T','L1V','L1W','L1X','L1Y','L1Z','L3P','L3R','L3S','L3T',
          'L3X','L3Y','L4A','L4B','L4C','L4E','L4G','L4H','L4J','L4K','L4L','L4S','L4T','L4V','L4W','L4X','L4Y','L4Z',
          'L5A','L5B','L5C','L5E','L5G','L5H','L5J','L5K','L5L','L5M','L5N','L5P','L5R','L5S','L5T','L5V','L5W','L6A',
          'L6B','L6C','L6E','L6G','L6H','L6J','L6K','L6L','L6M','L6P','L6R','L6S','L6T','L6V','L6W','L6X','L6Y','L6Z',
          'L7A','L7B','L7C','L7E','L7G','L7J','L7K','L7L','L7M','L7N','L7P','L7R','L7S','L7T','L8E','L8G','L8H','L8J',
          'L8K','L8L','L8M','L8N','L8P','L8R','L8S','L8T','L8V','L8W','L9A','L9B','L9C','L9G','L9H','L9K','L9L','L9N',
          'L9P','L9T','L0C','L0B','L0P','L0E','L0G','L0J','L0H']

uniqueGTA = {} #{'PostalCode': {'Latitude': 0, 'Longitude': 0, 'Count': 0, 'Place Name': ''}

for postalcode, count, fsa, lat, lng, place in uniquePC.values:
    if fsa in gtafsa:
        uniqueGTA[postalcode] = {'Count': count, 'FSA': fsa, 'Latitude': lat, 'Longitude': lng, 'Place Name': place}


writer = pd.ExcelWriter('static/data/yuride_postalcodes_uniquegtapc.xlsx', engine='openpyxl')
uniqueGTA = pd.DataFrame(uniqueGTA).T
uniqueGTA.to_excel(writer, sheet_name='Unique GTA PC')

writer.save()
writer.close()

print(len(uniqueGTA))
'''

'''
detailedPC = pd.read_excel(open('static/data/yuride_postalcodes_filtered-master.xlsx', 'rb'),
                           sheetname='Detailed PC') #change sheetname for respective affialation sheet name

gtafsa = ['M1B','M1C','M1E','M1G','M1H','M1J','M1K','M1L','M1M','M1N','M1P','M1R','M1S','M1T','M1V','M1W','M1X','M2H',
          'M2J','M2K','M2L','M2M','M2N','M2P','M2R','M3A','M3B','M3C','M3H','M3J','M3K','M3L','M3M','M3N','M4A','M4B',
          'M4C','M4E','M4G','M4H','M4J','M4K','M4L','M4M','M4N','M4P','M4R','M4S','M4T','M4V','M4W','M4X','M4Y','M5A',
          'M5B','M5C','M5E','M5G','M5H','M5J','M5K','M5L','M5M','M5N','M5P','M5R','M5S','M5T','M5V','M5W','M5X','M6A',
          'M6B','M6C','M6E','M6G','M6H','M6J','M6K','M6L','M6M','M6N','M6P','M6R','M6S','M7A','M7R','M7Y','M8V','M8W',
          'M8X','M8Y','M8Z','M9A','M9B','M9C','M9L','M9M','M9N','M9P','M9R','M9V','M9W','L1B','L1C','L1E','L1G','L1H',
          'L1J','L1K','L1L','L1M','L1N','L1P','L1R','L1S','L1T','L1V','L1W','L1X','L1Y','L1Z','L3P','L3R','L3S','L3T',
          'L3X','L3Y','L4A','L4B','L4C','L4E','L4G','L4H','L4J','L4K','L4L','L4S','L4T','L4V','L4W','L4X','L4Y','L4Z',
          'L5A','L5B','L5C','L5E','L5G','L5H','L5J','L5K','L5L','L5M','L5N','L5P','L5R','L5S','L5T','L5V','L5W','L6A',
          'L6B','L6C','L6E','L6G','L6H','L6J','L6K','L6L','L6M','L6P','L6R','L6S','L6T','L6V','L6W','L6X','L6Y','L6Z',
          'L7A','L7B','L7C','L7E','L7G','L7J','L7K','L7L','L7M','L7N','L7P','L7R','L7S','L7T','L8E','L8G','L8H','L8J',
          'L8K','L8L','L8M','L8N','L8P','L8R','L8S','L8T','L8V','L8W','L9A','L9B','L9C','L9G','L9H','L9K','L9L','L9N',
          'L9P','L9T','L0C','L0B','L0P','L0E','L0G','L0J','L0H']

detailedGTAPC = [] #{'PostalCode': '', 'FSA': '', 'Latitude': 0, 'Longitude': 0,'Place Name': '', 'Affiliation': ''}

for aff, fsa, lat, lng, place, postalcode in detailedPC.values:
    if fsa in gtafsa:
        detailedGTAPC.append({'PostalCode': postalcode, 'FSA': fsa,
                               'Latitude': lat, 'Longitude': lng,
                               'Place Name': place, 'Affiliation': aff})

writer = pd.ExcelWriter('static/data/yuride_postalcodes_uniquegtapc.xlsx', engine='openpyxl')
detailedGTAPC = pd.DataFrame(detailedGTAPC)
detailedGTAPC.to_excel(writer, sheet_name='Detailed GTA PC')

writer.save()
writer.close()

print(len(detailedGTAPC))
'''