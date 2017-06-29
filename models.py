from app import db

class Post(db.Model):

	__tablename__ = "posts"

	# id_db = db.Column(db.Integer, nullable=False)
	title = db.Column(db.String, nullable=False)
	link = db.Column(db.String, nullable=False, unique=True, primary_key=True)
	date_posted = db.Column(db.DateTime(timezone=False), nullable=False)
	site = db.Column(db.String, nullable=False)
	origin = db.Column(db.String, nullable=False)
	origin_airport = db.Column(db.String, nullable=True)
	destination = db.Column(db.String, nullable=False)
	destination_airport = db.Column(db.String, nullable=True)
	carrier = db.Column(db.String, nullable=True)
	price = db.Column(db.Integer, nullable=False)
	ticket_type = db.Column(db.String, nullable=True)
	currency = db.Column(db.String, nullable=True)
	reverse = db.Column(db.String, nullable=True)

	def __init__(self, title, link, date_posted, site, origin, origin_airport, destination, destination_airport, carrier, price, ticket_type, currency, reverse):
		self.title = title
		self.link = link
		self.date_posted = date_posted
		self.site = site
		self.origin = origin
		self.origin_airport = origin_airport
		self.destination = destination
		self.destination_airport = destination_airport
		self.carrier = carrier
		self.price = price
		self.ticket_type = ticket_type
		self.currency = currency
		self.reverse = reverse

	# def __repr__(self):
	# 	return "{} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.title, self.link, self.date_posted, self.site, self.origin, self.origin_airport, self.destination, self.destination_airport, self.carrier, self.price, self.ticket_type, self.currency, self.reverse)