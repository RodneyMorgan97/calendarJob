#source 28

from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions


def getJSON():
	try:
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
		req = urllib2.Request('https://womensnetworkneohio.com/Events?EventViewMode=1&EventListViewMode=1', headers=hdr)
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page, "html.parser")
		event = soup.find_all("div", {'class' : 'boxInfoContainer'})
		title = soup.find_all("h4", {'class' : 'boxHeaderTitle'})

		toJSON = []

		for i in range(len(event)):
			date = event[i].ul.li.div.get_text()
			date = helperFunctions.monthToNum(date[ : date.find(' ')]) + '-' + date[date.find(' ') + 1 : date.find(',')]
			
			time = event[i].ul.li.next_sibling.next_sibling.div.span.get_text()
			time = time[ :time.find('-')].strip().lower().replace(' ', '')

			location = event[i].ul.li.next_sibling.next_sibling.next_sibling.next_sibling.div.span.get_text()
			
			toJSON.append({
		 					'website':'noche.org/modules/calendar/calendar.php',
		 				  	'title' : title[i].get_text().replace('\n',''),
		 				  	'location' : location,
		 				  	'description' : '',
		 				  	'date' : date,
		 				  	'time' : time
		 				  })

		return toJSON

	except:
		return ''
