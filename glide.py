from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#haven't started
def getJSON():
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	req = urllib2.Request('http://www.glideit.org/news-and-events/events', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find_all("span" , {'itemprop' : 'name'})
	event = soup.find_all("div", {'class' : 'eb-category-1 eb-event clearfix'})
	description = soup.find_all("div", {'class' : 'eb-description-details span7'})

	toJSON = []
	 
	for i in range (len(event)):
		toJSON.append({
	 					'website':'http://www.glideit.org/news-and-events/events',
	 				  	'title' : event[i].div.h2.a.span.get_text(),
	 				  	'location' : '',
	 				  	'description' : description[0].get_text(),
	 				  	'date' : '',
	 				  	'time' : ''
	 				  })