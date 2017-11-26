#First Source on the list
from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions

def getJSON():
	try:
		page = urllib2.urlopen('http://akronsbdc.org/calendar/')
		soup = BeautifulSoup(page, "html.parser")
		title = soup.find_all("span", {'class' : 'ai1ec-event-title'})
		location = soup.find_all("span", {'class' : 'ai1ec-event-location'})
		description = soup.find_all("div", {'class' : 'ai1ec-event-description'})
		month = soup.find_all("div", {'class' : 'ai1ec-month'})
		day = soup.find_all("div", {'class' : 'ai1ec-day'})
		time = soup.find_all("div", {'class' : 'ai1ec-event-time'})

		toJSON = []

		for i in range(len(title)):
			eventTime = time[i].string.strip()
			if(eventTime.find("am") == -1):
				eventTime = eventTime[eventTime.find("@") + 2 : eventTime.find("pm") + 2]
			else:
				eventTime = eventTime = eventTime[eventTime.find("@") + 2 : eventTime.find("am") + 2]
			eventTime = eventTime[ : eventTime.find(" ")] + eventTime[eventTime.find(" ") + 1 : ]
		 	toJSON.append({
		 					'website':'http://akronsbdc.org/calendar/',
		 				  	'title' : title[i].get_text().replace(location[i].get_text(), '').replace('\n', '').replace('\t',''),
		 				  	'location' : location[i].string.strip(),
		 				  	'description' : description[i].get_text().replace('\n', ''),
		 				  	'date' : (helperFunctions.monthToNum(month[i].string.strip()) + '-' + day[i].string.strip()),
		 				  	'time' : eventTime
		 				  })

		return toJSON

	except:
		return ''