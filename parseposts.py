import requests
import json

def get_entity(entities, entity_name):
	value = entities.get(entity_name,None)
	if value:
		return value[0]["value"]
	else: 
		return None


def get_post_details(entities):

	post_details = {
		"origin": "",
		"origin_airport": "",
		"destination": "",
		"destination_airport": "",
		"carrier": "",
		"amount_of_money": "",
		"ticket_type": "",
		"currency": "",
		"reverse": ""
	}

	for key in entities:
		post_details[key] = get_entity(entities, key)
	for key in post_details:
		if post_details[key] == "":
			post_details[key] = None

	return post_details


def parse_post(message):

	headers = {
    'Authorization': 'Bearer DAEL2C6SQE4VKUGWYEHPROSSJGJ2Z5FP',
	}

	params = (
	    ('v', '20170621'),
	    ('q', message),
	)

	result = requests.get('https://api.wit.ai/message', headers=headers, params=params)
	
	if result:
		data = json.loads(result.text)
		entities = data["entities"]
		post_object = get_post_details(entities)
		# print(post_object) # for debugging

		return post_object

# parse_post("Non-stop, summer, Christmas and New Year flights from Calgary, Canada to Mexico City, Mexico for only $388 CAD roundtrip with Aeromexico.")








