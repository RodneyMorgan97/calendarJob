#source 13

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
	req = urllib2.Request('https://www.kent.edu/yourtrainingpartner/calendar-program-offerings', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find_all("div" , {'class' : 'views-field views-field-title'})
	date = soup.find_all("span", {'class' : 'date-display-single'})
	parsedDate = []

	for x in range (len(date)):
		if ((x % 2) == 0):
			parsedDate.append(date[x])

	toJSON = []

	for i in range (len(title)):
	
		for a in title[i].find_all('a', href=True):
			page = urllib2.urlopen('https://www.kent.edu' + a['href'])
			soup = BeautifulSoup(page, "html.parser")

		description = soup.find('meta', {'name' : 'description'})
		thisTime = helperFunctions.removeDayOfWeek(parsedDate[i].get_text()).lstrip()
		location = soup.find('div', {'class' : 'views-field views-field-field-price'})
		thisDate = helperFunctions.monthToNum(thisTime[:thisTime.find(' ')]) + '-' + thisTime[thisTime.find(' ') + 1: thisTime.find(',')]
		thisTime = thisTime[thisTime.find(':') - 2 : thisTime.find(':') + 7].lstrip()
		

		

		toJSON.append({
	 					'website':'www.kent.edu/yourtrainingpartner/calendar-program-offerings',
	 				  	'title' : title[i].get_text(),
	 				  	'location' : '',
	 				  	'description' : description['content'],
	 				  	'date' : thisDate,
	 				  	'time' : thisTime
	 				  })

	return json.dumps(toJSON)

