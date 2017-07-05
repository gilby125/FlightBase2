from flask import Flask, render_template, g
from FlightBot import create_flight_object, get_post_links, get_page_content
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# import sqlite3


# CREATE APPLICATION OBJECT

app = Flask(__name__)

# CONFIG
import os
app.config.from_object(os.environ["APP_SETTINGS"])



# app.database = "main.db"

#CREATE THE SQLALCHEMY OBJECT

db = SQLAlchemy(app)
from models import *


@app.route('/')
@app.route('/index')

def index():
	# posts = create_flight_object(get_post_links(get_page_content("https://www.theflightdeal.com/")))
	
	# p = db.session.query(Post).all
	posts = []
	for row in db.session.query(Post).all():
		if len(posts) < 50:
			post = {
				"title": row.title,
				"link": row.link,
				"date_posted": row.date_posted.strftime("%b %-d"),
				"site": row.site,
				"origin": row.origin,
				"origin_airport": row.origin_airport,
				"destination": row.destination,
				"destination_airport": row.destination_airport,
				"carrier": row.carrier,
				"price": row.price,
				"ticket_type": row.ticket_type,
				"currency": row.currency,
				"reverse": row.reverse,
			}

			posts.append(post)

	return render_template("index.html", title='Home', posts=posts)

# def connect_db():
# 	return sqlite3.connect(app.database)

#  (id_db INTEGER PRIMARY KEY AUTOINCREMENT,
	# title TEXT,
	# date_posted TEXT,
	# link TEXT,
	# site TEXT, 
	# origin TEXT,
	# origin_airport TEXT,
	# destination TEXT,
	# destination_airport TEXT,
	# carrier TEXT,
	# price INTEGER NOT NULL,
	# ticket_type TEXT,
	# currency TEXT,
	# reverse TEXT)""")

if __name__ == '__main__':

	app.run()







	