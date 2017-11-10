#source 21

from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone


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

	g = open('RadSchedulerExport.ics','rb')
	gcal = Calendar.from_ical(g.read())
	for component in gcal.walk():
	    if component.name == "VEVENT":
	    	date = component.get('DTSTART')

	    	toJSON.append({
	 					'website':'www.kent.edu/yourtrainingpartner/calendar-program-offerings',
	 				  	'title' : component.get('SUMMARY'),
	 				  	'location' : '',
	 				  	'description' : component.get('DESCRIPTION'),
	 				  	'date' : '',
	 				  	'time' : ''
	 				  })

	g.close()

	
	return

	
