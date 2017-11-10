#source 12

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
	req = urllib2.Request('https://www.eventbrite.com/o/launchnet-kent-state-university-4732963441', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find_all("div", {'class' : 'list-card__title'})
	location = soup.find_all("div" , {'class' : 'list-card__venue'})
	date = soup.find_all("time" , {'class' : 'list-card__date'})
	toJSON = []



	thisDate = date[0].get_text().replace(' ', '').strip()
	time = thisDate[thisDate.find('\n') + 1:]
	

	for i in range (len(title)):

		dateAndTime = date[i].get_text().replace(' ', '').strip()
		thisDate = dateAndTime[dateAndTime.find(',') + 1 : dateAndTime.find('\n')]
		thisDate = helperFunctions.monthToNum(thisDate[:3]) + '-' + thisDate[3:]
		thisDate= thisDate.replace('Mul-tipleDate', 'Multiple Dates')
		thisTime = dateAndTime[dateAndTime.find('\n') + 1 : ].lower().replace('multipledates', '')



		
		
		toJSON.append({
	 					'website':'www.eventbrite.com/o/launchnet-kent-state-university-4732963441',
	 				  	'title' : title[i].get_text().strip(),
	 				  	'location' : location[i].get_text().strip(),
	 				  	'description' : '',
	 				  	'date' : thisDate,
	 				  	'time' : thisTime
	 				  })
	return toJSON