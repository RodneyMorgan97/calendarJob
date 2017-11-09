#source 24

from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions
from datetime import datetime


def getJSON():
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	req = urllib2.Request('http://noche.org/modules/calendar/calendar.php', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find_all("span", {'class' : 'event-title'})
	location = soup.find_all("span" , {'class' : 'tip-container'})
	date = soup.find_all("ul" , {'class' : 'eventlist'})
	

	toJSON=[]
	
	for i in range (len(title)):
		timeAndDate = location[i].get_text()
		time = timeAndDate[timeAndDate.find('Time: ') : timeAndDate.find('-')].replace('Time: ', '').replace(' ','').strip().lower()
		location = timeAndDate[timeAndDate.find('Location: ') : ].replace('Location: ', '')
		location = location[ : location.find('\n')]
		day = date[i].parent.find("div" , {'class' : 'date'}).get_text()
		
		thisDate =  str(helperFunctions.monthToNum(datetime.now().month)) + '-' + day

		toJSON.append({
	 					'website':'noche.org/modules/calendar/calendar.php',
	 				  	'title' : title[i].get_text(),
	 				  	'location' : location,
	 				  	'description' : '',
	 				  	'date' : thisDate,
	 				  	'time' : time
	 				  })
	return json.dumps(toJSON)
