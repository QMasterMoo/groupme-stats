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

def getMessages(groupID, payload):
	messagesRaw = getResponse(requests.get(api_URL + '/groups/' + groupID + '/messages' + api_key, params=payload))
	messages = []
	for message in messagesRaw['messages']:
		messages.append((message['id'], message['text']))
	return messages

def getAllMessages(groupID, payload):
	payload['limit'] = 20
	messages = getMessages(groupID, payload)
	allMessages = messages
	count = len(allMessages)
	while count == 20: #20 is defalt request size
		payload['before_id'] = messages[0][0]
		messages = getMessages(groupID, payload)
		allMessages += messages
		count = len(messages)
	return allMessages

#DO THINGS HERE
groupID = ""

payload = {'limit' : 20}
print(getAllMessages(groupID, payload))
#getAllMessages(groupID, payload)