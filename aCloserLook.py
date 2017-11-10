#source 23

from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions


def getJSON():
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	req = urllib2.Request('https://www.summitartspace.org/calendar/', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find_all("")	
	event = soup.find_all("div", {'class' : 'css-events-list' })
	

	allTBody = event[0].find_all('tbody')

	toJSON = []

	for tBody in allTBody:
		for tR in tBody:
			dateAndTime = tR.td.get_text()
			title = tR.td.next_sibling.next_sibling.a.get_text()
			location = tR.td.next_sibling.next_sibling.i.get_text()
			dateAndTime = dateAndTime.strip()
			date = dateAndTime[:5].replace('/', '-')
			time = dateAndTime[dateAndTime.find('\n') + 1 : ].strip()
			time = time[ : time.find('-')].strip().replace(' ','')


			toJSON.append({
	 					'website':'https://www.summitartspace.org/calendar/',
	 				  	'title' : title,
	 				  	'location' : location,
	 				  	'description' : '',
	 				  	'date' :  date,
	 				  	'time' : time
	 				  })
	return json.dumps(toJSON)
	

		
