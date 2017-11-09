#source 15

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
	req = urllib2.Request('https://www.kent.edu/vcd/news-archive', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	event = soup.find_all("div", {'class' : 'panel-panel panel-col'})

	toJSON = []

	for i in range (len(event)):

		date = event[i].get_text().strip()
		date = helperFunctions.removeDayOfWeek(date[date.find('\n') + 1 : ].strip()).strip()
		thisDate = helperFunctions.monthToNum(date[:date.find(' ')]) + '-' + date[date.find(' ') + 1: date.find(',')]
		thisTime = date[date.find("-") + 2 :]

		toJSON.append({

	 					'website':'https://www.kent.edu/vcd/news-archive',
	 				  	'title' : event[0].div.h3.get_text().strip(),
	 				  	'location' : '',
	 				  	'description' : '',
	 				  	'date' : thisDate,
	 				  	'time' : thisTime
	 				  })
	return json.dumps(toJSON)