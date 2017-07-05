# crowdsourcing cheap flights - people submit flights, if flights get booked, they get a commission.

import requests
from bs4 import BeautifulSoup
from daterangeparser import parse as date_range_parse
import dateparser
from datetime import datetime
# from opencage.geocoder import OpenCageGeocode
from parseposts import parse_post

# key = 'bd77884a840745deb60de7611ae68ec8'
# geocoder = OpenCageGeocode(key)


# import library to read webpages
# import library to understand locations
# import library to read dates
# import library to parse locations to understand ontology e.g. if user inputs Vancouver, it returns a location object that includes British Columbia, Canada, North America, etc.
# import library of airlines plus alliances

# country to continent https://pypi.python.org/pypi/incf.countryutils

# ================== COMPLETED V2 ==================

def get_page_content(link):
	result = requests.get(link)

	page = {
		"link": link,
		"content": result.content
	}

	return page

# FOR BLOGS WITH NO RSS FEED

def get_post_links(page):
	soup = BeautifulSoup(page["content"]) #,"lxml")
	site = page["link"].split(".")[1]

	resource = {
		"site": "",
		"posts": []
	}

#	==== FOR SECRET FLYING ====

	if site == "secretflying":
		for post in soup.findAll("article", id=True):

			p = {
				"link": "",
				"title": "",
				"date": ""
			}

			# p["title"] = "" #post.findAll("h2", { "class" : "entry-title"})[0].get_text().replace("\n","").replace("/", " or ")
			p["date"] = dateparser.parse(post.findAll("time", { "class" : "entry-date"})[0].get_text().replace("\n",""))
			p["link"] = post.findAll("h2", { "class" : "entry-title"})[0].findAll("a", href=True)[0]['href']

			# Navigates to actual post to get intro text which has more info than just the title (like carrier)
			post_page_content = get_page_content(p["link"])["content"]
			post_page_details = BeautifulSoup(post_page_content) #,"lxml")

			for i in post_page_details.findAll("div", { "class" : "entry-content" }):
				p["title"] = i.findAll('p')[0].getText().replace("\n", " ").replace("\xa0", " ").split("DEPART:")[0]

			resource["posts"].append(p)
			resource["site"] = "Secret Flying"
		
		return resource

#	==== FOR THE FLIGHT DEAL ====

	elif site == "theflightdeal":
		for div in soup.findAll("div", { "class" : "featured_post_slider"}): 
   			div.decompose()

		for post in soup.findAll("div", { "class" : "post-entry"}):

			p = {
				"link": "",
				"title": "",
				"date": ""
			}

			p["title"] = post.findAll("h1", { "class" : "post-title"})[0].get_text().replace("\n","").replace("/", " or ")
			p["date"] = dateparser.parse(post.findAll("span", { "class" : "date-container"})[0].get_text().replace("\n",""))
			p["link"] = post.findAll("h1", { "class" : "post-title"})[0].findAll("a", href=True)[0]['href']
			
			resource["posts"].append(p)
			resource["site"] = "The Flight Deal"

		return resource

#	==== FOR AIRFARE WATCHDOG ====

	elif site == "airfarewatchdog":
		for post in soup.findAll("li", { "class" : "category-list__entry"}):
			for link in post.findAll('a', href=True):

				p = {
				"link": "",
				"title": "",
				"date": ""
				}

				p["title"] = post.findAll("div", { "class" : "category-list__entry_leadin"})[0].get_text().replace("/", " or ")
				p["date"] = dateparser.parse(post.findAll("div", { "class" : "category-list__entry_date"})[0].get_text())
				p["link"] = "http://www.airfarewatchdog.com" + post.findAll('a', href=True)[0]['href']
				
				resource["posts"].append(p)
				resource["site"] = "Airfare Watchdog"

		return resource

# Use these links to test:
# http://www.airfarewatchdog.com/blog/by-category/20531381/fare-deal/
# https://www.secretflying.com/canada-deals/
# https://www.theflightdeal.com/


# ================== WORK IN PROGRESS V2 ==================

def create_flight_object(resource):

	r = []
	site = resource["site"]
	for post in resource["posts"]:
		post_object = {
			"title": post["title"],
			"date": post["date"],
			"link": post["link"],
			"site": site,
			"details": [parse_post(post["title"])]
		}
		r.append(post_object)

	return r

# create_flight_object(get_post_links(get_page_content("https://www.theflightdeal.com/")))

def get_posts(link):
	page = get_page_content(link)
	content = get_post_links(page)
	flights = create_flight_object(content)
	return flights

# print(get_post_links(get_page_content("https://www.secretflying.com/canada-deals/")))



# Parse titles
#	Return Flight Object
# Match Origin
# Match Destination
# Match Price



# ================== COMPLETED V1 ==================



# def sf_get_post_content(link):
# 	soup = BeautifulSoup(get_page_content(link),"lxml")
# 	post_content = []
# 	date_ranges = []

# 	for div in soup.findAll("div", { "class" : "entry-content" }):
# 		text = div.findAll('p')
# 		for p in text:
# 			p = p.getText()
# 			p = p.replace("\n", " ")
# 			post_content.append(p)

# 	for div in soup.findAll("div", { "class" : "entry-content" }):
# 		text = div.findAll('p')
# 		for p in text:
# 			links = p.findAll('a')
# 			for a in links:
# 				result = a.getText()
# 				date_ranges.append(result)

# 	while "\xa0" in post_content: post_content.remove("\xa0")
# 	while "\xa0" in date_ranges: date_ranges.remove("\xa0")

# 	for item in post_content:
# 		item.replace("\xa0", " ")

# 	description = post_content[0]
# 	origin = ""
# 	destination = ""
# 	final = ""
# 	stops = ""
# 	dates = ""
# 	ex_dates = date_ranges
# 	price = ""
# 	price_description = ""
# 	currency = ""
# 	airline = ""
# 	link = link

# 	for item in post_content:
# 		if "DEPART:" in item:
# 			origin = item.split(":")[1]

# 		if "ARRIVE:" in item:
# 			destination = item.split(":")[1]

# 		if "RETURN:" in item:
# 			final = item.split(":")[1]

# 		if "STOPS:" in item:
# 			stops = item.split(":")[1]

# 		if "AVAILABILITY:" in item:
# 			dates = item.split(":")[1]

# 	if "$" in description:
# 		index_start = description.find("$")
# 		index_end = description.lower().find("roundtrip") + 9
# 		price_description = description[index_start:index_end]
# 		price = int(price_description.split()[0][1:])
# 		if len(price_description.split()[2]) == 3:
# 			currency = price_description.split()[2]

# 	post_object = {
# 		"description": description,
# 		"origin": origin,
# 		"destination": destination,
# 		"final": final,
# 		"stops": stops,
# 		"dates": dates,
# 		"ex_dates": ex_dates,
# 		"price_description": price_description,
# 		"price": price,
# 		"currency": currency,
# 		"airline": airline,
# 		"link": link
# 	}
# 	print(post_object["dates"])
# 	print(post_object["ex_dates"])
# 	return post_object


# def parse_date_ranges(date):
# 	start, end = date_range_parse(date)
# 	date_range = [start, end]

# 	return date_range


# def price_match(ref_price, max_price):
# 	if ref_price < max_price:
# 		return True


# def date_range_list_match(ref, dates):
# 	for r in ref:
# 		ref_range = parse_date_ranges(r)
# 		ref_range_start = ref_range[0]
# 		ref_range_end = ref_range[1]

# 		user_range_start = dateparser.parse(dates[0])
# 		user_range_end = dateparser.parse(dates[1])

# 		if ref_range_start >= user_range_start and ref_range_end <= user_range_end:
# 			return True

# 	return False


# def location_match(ref, place):
# 	for r in ref:
# 		for p in place:

# 			ref_place = geocoder.geocode(r)[0]["components"]
# 			input_place = geocoder.geocode(p)[0]["components"]

# 			if 'city' in ref_place.keys() and 'city' in input_place.keys():
# 				ref_city = ref_place["city"]
# 				input_city = input_place["city"]
# 				if ref_city == input_city:
# 					return True

# 			elif 'country' in ref_place.keys() and 'country' in input_place.keys():
# 				ref_country = ref_place["country"]
# 				input_country = input_place["country"]
# 				if ref_country == input_country:
# 					return True

# 			else:
# 				return False

# 		return False


# # def location_list_match(ref, place_list):
# # 	matches = []
# # 	for place in plast_list:
# # 		matches.append(location_match(ref, place))

# # 	if any(matches):
# # 		return True
# # 	else:
# # 		return False


# def post_match(post_params, user_params):

# 	post_origin = []
# 	post_origin.append(post_params["origin"])
# 	post_destination = []
# 	post_destination.append(post_params["destination"])
# 	post_dates = post_params["ex_dates"]
# 	post_price = post_params["price"]

# 	user_origin = user_params["origin"]
# 	user_destination = user_params["destination"]
# 	user_dates = user_params["date_range"]
# 	user_price = user_params["max_price"]

# 	match_parameters = []

# 	# origin
# 	match_parameters.append(location_match(post_origin, user_origin))

# 	# destination
# 	match_parameters.append(location_match(post_destination, user_destination))

# 	# dates
# 	match_parameters.append(date_range_list_match(post_dates, user_dates))

# 	# price
# 	match_parameters.append(price_match(post_price, user_price))

# 	print(post_params["description"])
# 	print(match_parameters)
# 	if all(match_parameters):
# 		return True
# 	else:
# 		return False


# # ================== WORK IN PROGRESS ==================


# user_params = {
# 	"origin": ["Edmonton", "Calgary", "Vancouver", "Toronto"],
# 	"destination": ["Japan", "Tokyo", "Hong Kong", "Singapore", "Phillipines", "Taiwan"],
# 	"date_range": ["August 1", "October 15th"],
# 	"max_price": 600
# }

# links = get_post_links(get_page_content("https://www.secretflying.com/canada-deals/"))[3]
# post_object = sf_get_post_content(links)
# post_match(post_object, user_params)

# message = []

# # for link in links:
# # 	post_object = sf_get_post_content(link)
# # 	if post_match(post_object, user_params):
# # 		post_description = post_object["description"]
# # 		post_link = post_object["link"]

# # 		summary = "{} ------- ({}) \n\n".format(post_description, post_link)
# # 		message.append(summary)

# print(message)

# def get_user_parameters(params):
# 	# ask user where they want to fly from
# 	# ask user where they want to fly to 
# 	# ask user date range they want to fly
# 	# ask user price range they're okay with (optional)

# 	# return params from user


# def post_matches_parameters(params, post_json):
# 	# if origin, destination, date range, (optional: price, airline), matches user parameters

# 	# return true



# ==================







# country_continents = {
# 	"AD": "Europe",
# 	"AE": "Asia",
# 	"AF": "Asia",
# 	"AG": "North America",
# 	"AI": "North America",
# 	"AL": "Europe",
# 	"AM": "Asia",
# 	"AN": "North America",
# 	"AO": "Africa",
# 	"AQ": "Antarctica",
# 	"AR": "South America",
# 	"AS": "Australia",
# 	"AT": "Europe",
# 	"AU": "Australia",
# 	"AW": "North America",
# 	"AZ": "Asia",
# 	"BA": "Europe",
# 	"BB": "North America",
# 	"BD": "Asia",
# 	"BE": "Europe",
# 	"BF": "Africa",
# 	"BG": "Europe",
# 	"BH": "Asia",
# 	"BI": "Africa",
# 	"BJ": "Africa",
# 	"BM": "North America",
# 	"BN": "Asia",
# 	"BO": "South America",
# 	"BR": "South America",
# 	"BS": "North America",
# 	"BT": "Asia",
# 	"BW": "Africa",
# 	"BY": "Europe",
# 	"BZ": "North America",
# 	"CA": "North America",
# 	"CC": "Asia",
# 	"CD": "Africa",
# 	"CF": "Africa",
# 	"CG": "Africa",
# 	"CH": "Europe",
# 	"CI": "Africa",
# 	"CK": "Australia",
# 	"CL": "South America",
# 	"CM": "Africa",
# 	"CN": "Asia",
# 	"CO": "South America",
# 	"CR": "North America",
# 	"CU": "North America",
# 	"CV": "Africa",
# 	"CX": "Asia",
# 	"CY": "Asia",
# 	"CZ": "Europe",
# 	"DE": "Europe",
# 	"DJ": "Africa",
# 	"DK": "Europe",
# 	"DM": "North America",
# 	"DO": "North America",
# 	"DZ": "Africa",
# 	"EC": "South America",
# 	"EE": "Europe",
# 	"EG": "Africa",
# 	"EH": "Africa",
# 	"ER": "Africa",
# 	"ES": "Europe",
# 	"ET": "Africa",
# 	"FI": "Europe",
# 	"FJ": "Australia",
# 	"FK": "South America",
# 	"FM": "Australia",
# 	"FO": "Europe",
# 	"FR": "Europe",
# 	"GA": "Africa",
# 	"GB": "Europe",
# 	"GD": "North America",
# 	"GE": "Asia",
# 	"GF": "South America",
# 	"GG": "Europe",
# 	"GH": "Africa",
# 	"GI": "Europe",
# 	"GL": "North America",
# 	"GM": "Africa",
# 	"GN": "Africa",
# 	"GP": "North America",
# 	"GQ": "Africa",
# 	"GR": "Europe",
# 	"GS": "Antarctica",
# 	"GT": "North America",
# 	"GU": "Australia",
# 	"GW": "Africa",
# 	"GY": "South America",
# 	"HK": "Asia",
# 	"HN": "North America",
# 	"HR": "Europe",
# 	"HT": "North America",
# 	"HU": "Europe",
# 	"ID": "Asia",
# 	"IE": "Europe",
# 	"IL": "Asia",
# 	"IM": "Europe",
# 	"IN": "Asia",
# 	"IO": "Asia",
# 	"IQ": "Asia",
# 	"IR": "Asia",
# 	"IS": "Europe",
# 	"IT": "Europe",
# 	"JE": "Europe",
# 	"JM": "North America",
# 	"JO": "Asia",
# 	"JP": "Asia",
# 	"KE": "Africa",
# 	"KG": "Asia",
# 	"KH": "Asia",
# 	"KI": "Australia",
# 	"KM": "Africa",
# 	"KN": "North America",
# 	"KP": "Asia",
# 	"KR": "Asia",
# 	"KW": "Asia",
# 	"KY": "North America",
# 	"KZ": "Asia",
# 	"LA": "Asia",
# 	"LB": "Asia",
# 	"LC": "North America",
# 	"LI": "Europe",
# 	"LK": "Asia",
# 	"LR": "Africa",
# 	"LS": "Africa",
# 	"LT": "Europe",
# 	"LU": "Europe",
# 	"LV": "Europe",
# 	"LY": "Africa",
# 	"MA": "Africa",
# 	"MC": "Europe",
# 	"MD": "Europe",
# 	"ME": "Europe",
# 	"MG": "Africa",
# 	"MH": "Australia",
# 	"MK": "Europe",
# 	"ML": "Africa",
# 	"MM": "Asia",
# 	"MN": "Asia",
# 	"MO": "Asia",
# 	"MP": "Australia",
# 	"MQ": "North America",
# 	"MR": "Africa",
# 	"MS": "North America",
# 	"MT": "Europe",
# 	"MU": "Africa",
# 	"MV": "Asia",
# 	"MW": "Africa",
# 	"MX": "North America",
# 	"MY": "Asia",
# 	"MZ": "Africa",
# 	"NA": "Africa",
# 	"NC": "Australia",
# 	"NE": "Africa",
# 	"NF": "Australia",
# 	"NG": "Africa",
# 	"NI": "North America",
# 	"NL": "Europe",
# 	"NO": "Europe",
# 	"NP": "Asia",
# 	"NR": "Australia",
# 	"NU": "Australia",
# 	"NZ": "Australia",
# 	"OM": "Asia",
# 	"PA": "North America",
# 	"PE": "South America",
# 	"PF": "Australia",
# 	"PG": "Australia",
# 	"PH": "Asia",
# 	"PK": "Asia",
# 	"PL": "Europe",
# 	"PM": "North America",
# 	"PN": "Australia",
# 	"PR": "North America",
# 	"PS": "Asia",
# 	"PT": "Europe",
# 	"PW": "Australia",
# 	"PY": "South America",
# 	"QA": "Asia",
# 	"RE": "Africa",
# 	"RO": "Europe",
# 	"RS": "Europe",
# 	"RU": "Europe",
# 	"RW": "Africa",
# 	"SA": "Asia",
# 	"SB": "Australia",
# 	"SC": "Africa",
# 	"SD": "Africa",
# 	"SE": "Europe",
# 	"SG": "Asia",
# 	"SH": "Africa",
# 	"SI": "Europe",
# 	"SJ": "Europe",
# 	"SK": "Europe",
# 	"SL": "Africa",
# 	"SM": "Europe",
# 	"SN": "Africa",
# 	"SO": "Africa",
# 	"SR": "South America",
# 	"ST": "Africa",
# 	"SV": "North America",
# 	"SY": "Asia",
# 	"SZ": "Africa",
# 	"TC": "North America",
# 	"TD": "Africa",
# 	"TF": "Antarctica",
# 	"TG": "Africa",
# 	"TH": "Asia",
# 	"TJ": "Asia",
# 	"TK": "Australia",
# 	"TM": "Asia",
# 	"TN": "Africa",
# 	"TO": "Australia",
# 	"TR": "Asia",
# 	"TT": "North America",
# 	"TV": "Australia",
# 	"TW": "Asia",
# 	"TZ": "Africa",
# 	"UA": "Europe",
# 	"UG": "Africa",
# 	"US": "North America",
# 	"UY": "South America",
# 	"UZ": "Asia",
# 	"VC": "North America",
# 	"VE": "South America",
# 	"VG": "North America",
# 	"VI": "North America",
# 	"VN": "Asia",
# 	"VU": "Australia",
# 	"WF": "Australia",
# 	"WS": "Australia",
# 	"YE": "Asia",
# 	"YT": "Africa",
# 	"ZA": "Africa",
# 	"ZM": "Africa",
# 	"ZW": "Africa"
# 	}





