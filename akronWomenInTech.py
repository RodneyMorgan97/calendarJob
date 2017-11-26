#source 27

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
		req = urllib2.Request('https://www.meetup.com/Akron-Women-In-Tech/events/', headers=hdr)
		page = urllib2.urlopen(req)
		soup = BeautifulSoup(page, "html.parser")
		event = soup.find_all("div" , {'class' : 'eventContent'})
		eventTitle = soup.find_all("span" , {'class' : 'eventName summary'})
		toJSON = []

		for i in range(len(event)):
			thisDate = event[i].a.span['title']
			thisDate = helperFunctions.monthToNum(thisDate[:3]) + '-' + thisDate[thisDate.find(' ') + 1 : thisDate.find(',')]
			
			toJSON.append({
		 					'website' : 'https://www.meetup.com/Akron-Women-In-Tech/events',
		 				  	'title' : eventTitle[i].get_text().replace('\n' , '').strip(),
		 				  	'location' : '',
		 				  	'description' : '',
		 				  	'date' : thisDate,
		 				  	'time' : event[i].a.span.get_text().replace(' ','').lower()
		 				  })
		return toJSON
		
	except:
		return ''