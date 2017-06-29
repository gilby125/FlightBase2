from app import db
from models import Post

# CREATE THE DATABASE AND THE DB TABLES

test = {
	'title': 'American – $148: Dallas – Boston (and vice versa). Roundtrip, including all Taxes', 
	'link': 'http://www.theflightdeal.com/2017/06/22/american-148-dallas-boston-and-vice-versa-roundtrip-including-all-taxes/', 
	'site': 'theflightdeal', 
	'date': '22 Jun 2017',
	'details': [{
		'destination_airport': None, 
		'amount_of_money': 148, 
		'origin': 'Dallas', 
		'carrier': 'American Airlines', 
		'ticket_type': 'Roundtrip', 
		'currency': None, 
		'intent': 'Parse', 
		'reverse': 'True', 
		'origin_airport': None, 
		'destination': 'Boston'
		}]
	}

data = [
	test.get('title'),
	test.get('link'),
	test.get('date'),
	test.get('site'),
	test.get('details')[0].get("origin"),
	test.get('details')[0].get("origin_airport"),
	test.get('details')[0].get("destination"),
	test.get('details')[0].get("origin_airport"),
	test.get('details')[0].get("carrier"),
	test.get('details')[0].get("amount_of_money"),
	test.get('details')[0].get("ticket_type"),
	test.get('details')[0].get("currency"),
	test.get('details')[0].get("reverse")
]

db.create_all()


# INSERT

db.session.add(Post(*data))


# COMMIT CHANGES

db.session.commit()