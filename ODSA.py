#source 21

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
	req = urllib2.Request('https://development.ohio.gov/DSACalendar/', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find_all("div" , {'class' : 'rsAptContent'})

	toJSON = []

	for i in range(len(title)):
		toJSON.append({
	 					'website':'https://development.ohio.gov/DSACalendar/',
	 				  	'title' : title[i].get_text().replace('delete', '').strip(),
	 				  	'location' : '',
	 				  	'description' : '',
	 				  	'date' : '',
	 				  	'time' : ''
	 				  })
	return json.dumps(toJSON)

	
