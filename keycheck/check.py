#import json
import requests
import logging
import traceback

#Write a script that compares the values of result and height from the following two endpoints
urls=["https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken", "https://api.blockcypher.com/v1/eth/main"]

rsp = requests.get(urls[0])
response_dict = rsp.json()

#print(json.dumps(response_dict, indent=4, sort_keys=True))
result = response_dict["result"]
#print(result)

rsp = requests.get(urls[1])
response_dict = rsp.json()

#print(json.dumps(response_dict, indent=4, sort_keys=True))
height = response_dict["height"]
#print(height)

try:
    if(int(result) == int(height)):
        print ('equal')
    else:
        print ('not equal')
except Exception as e:
    logging.error(traceback.format_exc())
