from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#source 9
def getJSON():
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	req = urllib2.Request('http://www.greaterakronchamber.org/Connect/Events', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	event = soup.find_all("div", {'class' : 'cal-item'})

	
	toJSON = []

	for i in range(len(event)):
		thisEvent = str(event[i].a['data-ot']).replace('<strong>' , '').replace('</strong>', '').replace('<br />', '')
		eventName = thisEvent[:thisEvent.find('\n')]
		thisEvent = thisEvent.replace(eventName + '\n', '')
		dateAndTime = thisEvent.replace('Date: ', '')
		eventDate = dateAndTime[ : dateAndTime.find(' ') -5].replace('/','-')
		eventTime = dateAndTime[dateAndTime.find(' ') + 1 : dateAndTime.find('\n')].replace(' ','').lower()
		eventTime = eventTime[ : len(eventTime) - 5] + eventTime[len(eventTime) - 2 : ]
		location = dateAndTime[dateAndTime.find('\n') + 1 :].replace('Location: ', '')

		toJSON.append({
	 					'website':'http://www.greaterakronchamber.org/Connect/Events',
	 				  	'title' : thisEvent,
	 				  	'location' : location,
	 				  	'description' : '',
	 				  	'date' : eventDate,
	 				  	'time' : eventTime
	 				  })
	return toJSON

