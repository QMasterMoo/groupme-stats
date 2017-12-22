import requests

#Setup api key
api_URL = 'https://api.groupme.com/v3'
api_key = '?token='
with open('api.key', 'r') as f:
	api_key += f.read()

##################
#helper functions#
##################


def getResponse(response):
	"""Returns the 'response' portion of our api calls. Idea stolen from github.com/youyanggu"""
	return response.json()['response']


#DO THINGS HERE





payload = {'per_page' : 10}
r = getResponse(requests.get(api_URL + "/groups" + api_key, params=payload))

for group in r:
	print(group['name'], group['id'])