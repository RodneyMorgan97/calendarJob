#source 6
from bs4 import BeautifulSoup
import urllib2
import json
import ast
import helperFunctions


def getJSON():

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	req = urllib2.Request('https://www.summitomj.org/events', headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html.parser")
	script = soup.find_all("script" , {'type' : 'application/ld+json'})
	d = ast.literal_eval(script[2].get_text())

	toJSON = []

	for i in range(len(d)):
		date = d[i]['startDate']
		time = helperFunctions.militaryToStandard(date[11:16])
		description = d[i]['description']
		try:
			location = d[i]['location']['address']['streetAddress'] + ', ' + d[i]['location']['address']['addressLocality'] + ', ' + d[i]['location']['address']['addressRegion']
		except:
			location = '' 

		name = d[i]['name']
		
		date = date[5:10]

		toJSON.append({
	 					'website':'https://www.summitomj.org/events',
	 				  	'title' : name,
	 				  	'location' : location,
	 				  	'description' : description,
	 				  	'date' :  date,
	 				  	'time' : time
	 				  })

	return toJSON