# Test/Technical Support Engineer #

## Practical Task #1 ##
## Practical Part ##

You need to iterate through a list of URLs and check their availability. 
Conditions:
* The list of URLs is located in the file /urls.txt.
* A URL is considered available if its response code is not 5XX or 4XX.
* The check must be implemented as a Bash function, which should be called within the script.
* The function must accept the path to the file with URLs as its input parameter.
* If any service returns an unavailable response, stop further checks.

## Practical Task #2 ##

Write a Dockerfile to build the following project: https://github.com/anza-xyz/agave.

## Practical Task #3 ##
Write a script that compares the values of result and height from the following two endpoints:
* Key: result https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken
* Key: height https://api.blockcypher.com/v1/eth/main