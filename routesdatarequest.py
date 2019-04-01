import requests
import pandas as pd
import json
import time
import random
import math

def savedata(uniqueGTAPC, oldGTAPCRoutes, uniqueGTAPCRoutes, routesFound, routesMissing):
    writer = pd.ExcelWriter('static/data/yuride_postalcodes_gta_routes.xlsx', engine='openpyxl')

    uniqueGTAPC = pd.DataFrame(uniqueGTAPC).T
    uniqueGTAPC.to_excel(writer, sheet_name='Unique GTA Routes')

    oldGTAPCRoutes = pd.DataFrame(oldGTAPCRoutes)
    oldGTAPCRoutes.to_excel(writer, sheet_name='Unique GTA Detailed Routes')

    uniqueGTAPCRoutes = pd.DataFrame(uniqueGTAPCRoutes)
    uniqueGTAPCRoutes.to_excel(writer, sheet_name='Unique GTA Detailed Routes New')

    writer.save()
    writer.close()
    print(len(uniqueGTAPC), routesFound, routesMissing)

#uniqueGTAPC = pd.read_excel(open('static/data/yuride_postalcodes_filtered-master.xlsx', 'rb'),
#                                sheetname='Unique GTA')
xls = pd.ExcelFile(open('static/data/yuride_postalcodes_gta_routes.xlsx', 'rb'))
uniqueGTAPC = pd.read_excel(xls, sheetname='Unique GTA Routes')
oldGTAPCRoutes = pd.read_excel(xls, sheetname='Unique GTA Detailed Routes')
xls.close()

uniqueGTAPC = uniqueGTAPC.T.to_dict()
#example uniqueGTAPC = {'PostalCode': {'Count': count, 'FSA': fsa, 'Latitude': 0, 'Longitude': 0, 'Count': 0, 'Place Name': ''}

#key = 'A7FP1BzPfz5siKlXeHzdOXl2dhpdPhGS'
key = 's1GPmzw9tphzeUDyr7lmjvGWbbLS9Ef4' #'zi0urTwPkQa1SJa4pBek4qxq7dzoY3oT' #'YTsA0biDDXWO7D4ZARR5UeKBK2c7GNKn'
savedInException = False
routesFound = 0
routesMissing = 0
uniqueGTAPCRoutes = []
for pCode, pDetails in uniqueGTAPC.items():
    if type(pDetails['boundingBox']) is float:
        try:
            api_url = 'http://www.mapquestapi.com/directions/v2/optimizedroute?key=' + key \
                      + '&json={"locations":[' \
                      + '{"latLng":{"lat":' + str(pDetails['Latitude']) + ',"lng":' + str(pDetails['Longitude']) + '}},' \
                      + '{"latLng": { "lat": 43.7705, "lng": -79.50218}}' \
                      + '],"options":{"avoids":["Toll Road"],"maxRoutes": 1}}'
            # print(api_url)

            response = requests.get(url=api_url, verify=False, timeout=(60, 60))
            responseData = response.json()

            if responseData['info']['statuscode'] == 0:
                routesFound = routesFound + 1
                print('Found', routesFound)

                route = responseData['route']

                #print(responseData, route['distance'])
                #print(uniqueGTAPC[pCode])
                #print(route['distance'], route['time'], route['fuelUsed'])

                pDetails['boundingBox'] = json.dumps(route['boundingBox'])
                pDetails['distance'] = route['distance']
                pDetails['formattedTime'] = route['formattedTime']
                pDetails['fuelUsed'] = route['fuelUsed']
                pDetails['hasBridge'] = route['hasBridge']
                pDetails['hasHighway'] = route['hasHighway']
                pDetails['hasSeasonalClosure'] = route['hasSeasonalClosure']
                pDetails['hasTollRoad'] = route['hasTollRoad']
                pDetails['hasTunnel'] = route['hasTunnel']
                pDetails['hasUnpaved'] = route['hasUnpaved']

                pDetails['realTime'] = route['realTime']
                pDetails['locations'] = json.dumps(route['locations'])
                pDetails['time'] = route['time']

                pDetails['drivingStyle'] = route['options']['drivingStyle']
                pDetails['highwayEfficiency'] = route['options']['highwayEfficiency']
                pDetails['useTraffic'] = route['options']['useTraffic']

                uniqueGTAPCRoutes.append(responseData)
            else:
                routesMissing = routesMissing + 1
                print('Not Found', responseData['info']['messages'])
                #print('Not Found', routesMissing, 'ROUTE NOT FOUND', api_url)

            # sleep for 250-350 milliseconds until next request
            #time.sleep(random.uniform(.15, .25))
            time.sleep(.1)
            # sleep for random
            #if routesFound % 300 == 0:
            #    time.sleep(.5)
            #    #time.sleep(random.uniform(1, 3))
        except requests.exceptions.Timeout:
            print "Timeout occurred"
            savedata(uniqueGTAPC, oldGTAPCRoutes, uniqueGTAPCRoutes, routesFound, routesMissing)
            savedInException = True
        except requests.exceptions.ConnectionError:
            print "Connection Error"
            savedata(uniqueGTAPC, oldGTAPCRoutes, uniqueGTAPCRoutes, routesFound, routesMissing)
            savedInException = True
        except requests.exceptions.BaseHTTPError:
            print requests.exceptions.BaseHTTPError.message
            savedata(uniqueGTAPC, oldGTAPCRoutes, uniqueGTAPCRoutes, routesFound, routesMissing)
            savedInException = True

savedata(uniqueGTAPC, oldGTAPCRoutes, uniqueGTAPCRoutes, routesFound, routesMissing)
