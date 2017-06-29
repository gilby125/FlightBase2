from app import db
from models import Post
import sqlite3
from sqlalchemy import desc


# test = {
# 	'title': 'American – $148: Dallas – Boston (and vice versa). Roundtrip including all Taxes',
# 	'link': 'http://www.theflightdeal.com/2017/06/22/american-148-dallas-boston-and-vice-versa-roundtrip-including-all-taxes/',
# 	'site': 'theflightdeal',
# 	'date': '22 Jun 2017',
# 	'details': [{
# 		'destination_airport': None,
# 		'amount_of_money': 148,
# 		'origin': 'Dallas',
# 		'carrier': 'American Airlines',
# 		'ticket_type': 'Roundtrip',
# 		'currency': None,
# 		'intent': 'Parse',
# 		'reverse': 'True',
# 		'origin_airport': None,
# 		'destination': 'Boston'
# 		}]
# 	}


def insert(table, dictionary):

	title = dictionary.get('title')
	link = dictionary.get('link')
	date = dictionary.get('date')
	site = dictionary.get('site')
	origin = dictionary.get('details')[0].get("origin")
	origin_airport = dictionary.get('details')[0].get("origin_airport")
	destination = dictionary.get('details')[0].get("destination")
	destination_airport = dictionary.get('details')[0].get("destination_airport")
	carrier = dictionary.get('details')[0].get("carrier")
	price = dictionary.get('details')[0].get("amount_of_money")
	ticket_type = dictionary.get('details')[0].get("ticket_type")
	currency = dictionary.get('details')[0].get("currency")
	reverse = dictionary.get('details')[0].get("reverse")


	if origin != None and destination != None and carrier != None and price != None :

		data = [
			title,
			link,
			date,
			site,
			origin,
			origin_airport,
			destination,
			destination_airport,
			carrier,
			price,
			ticket_type,
			currency,
			reverse
		]

		db.session.merge(Post(*data))
		db.session.flush()
		db.session.commit()

def sort_desc():
	db.session.query(Post).order_by(desc(Post.date_posted))
	db.session.commit()


# COMMIT CHANGES

	# with sqlite3.connect("main.db") as connection:
	# 	c = connection.cursor()
	# 	fields = "title link date_posted site origin origin_airport destination destination_airport carrier price ticket_type currency reverse"
	# 		# cur.execute("INSERT INTO account_holder (emailusernamephonepassword) VALUES (????)" (emailusernamephonepassword))

	# 	query = 'INSERT OR IGNORE INTO %s (%s) VALUES (%s)' % (
	# 		table
	# 		fields
	# 		' '.join(['?'] * len(data))
	# 	)
	# 	c.execute(query data)
	# 	last_row = c.lastrowid

	# 	return last_row

# insert("posts" test)


# COMMENT THIS SECTION OUT AFTER TESTING

with sqlite3.connect("posts.db") as connection:
	c = connection.cursor()
	c.execute("""DROP TABLE posts""")

db.create_all()







