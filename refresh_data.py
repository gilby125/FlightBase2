from FlightBot import get_posts
from sql import insert, sort_desc

# ENTER TARGET WEBSITES TO SCRAPE. CURRENTLY SUPPORTS == SECRET FLYING == , == THE FLIGHT DEAL ==, AND == AIRFARE WATCHDOG ==

targets = [
	"http://www.airfarewatchdog.com/blog/by-category/20531381/fare-deal/",
	"https://www.secretflying.com/canada-deals/",
	"https://www.secretflying.com/usa-deals/",
	"https://www.theflightdeal.com/",
	"https://www.theflightdeal.com/page/2/",
	"https://www.theflightdeal.com/page/3/"
	]

def refresh(targets):
	for link in targets:
		print(link)
		flights = get_posts(link)
		for flight in flights:
			if flight.get('details')[0] != None:
				r = insert("posts", flight)
				print(r)

refresh(targets)
sort_desc()
