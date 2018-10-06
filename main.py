#! /usr/bin/env python
# Import packages
import sys
import os
import requests
import datetime
import json

# locate the root folder
root_folder_project = os.path.dirname((os.path.abspath(__file__)))
# add the root folder to sys path, this way the different modules can be imported by UNIX!
sys.path.insert(1, root_folder_project)

def get_CMC():

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    querystring = {"limit":"250","sort":"market_cap"}

    headers = {
        'X-CMC_PRO_API_KEY': "301b49be-b6db-46eb-b83a-0ab588e7215b",
        'Accept': "application/json",
        'Accept-Encoding': "deflate, gzip",
        'Cache-Control': "no-cache",
        'Postman-Token': "c7a8c4b4-287f-4021-93c4-8494b4e5885b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)

    data = response.json()
    print(type(data))

    folder = os.path.join(root_folder_project, 'data')
    filename = 'CMC_{}.json'.format(datetime.datetime.now().strftime("%Y%m%d_%H:%M"))
    path = os.path.join(folder, filename)
    with open(path, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)

get_CMC()







# with open('CMC_{}.json'.format(datetime.datetime.now()), 'w') as outfile:
#     json.dump(response.text, outfile)

# for coins in data['data']:
#     print(coins)

# print(response.text)

# Write to csv
# Run daily / 6 hours
# determine "climbers" (relative movers)