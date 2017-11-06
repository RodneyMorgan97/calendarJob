from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions

def getJSONAkron():
	page = urllib2.urlopen('https://www.ecdi.org/events/akron')
	soup = BeautifulSoup(page, "html.parser")
	event = soup.find_all("div", {'class' : 'row class-listing'})

	title = []
	description = []
	date = []
	toJSON = []

	for getEvent in event:
		title.append(getEvent.div.h4.get_text())
		date.append(getEvent.p.em.get_text())
		description.append(getEvent.p.next_sibling.next_sibling.get_text())

	for i in range(len(title)):
		thisDate = date[i]
		thisTime = thisDate[thisDate.find(':') - 2 : thisDate.find(':') + 6].lower()
		if(thisTime[0] == ' '):
			thisTime = thisTime[1:]
		if(thisTime[4] == ' '):
			thisTime = thisTime[:4] + thisTime[5:]
		if(thisTime[5] == ' '):
			thisTime = thisTime[:5] + thisTime[6:]
		if((thisTime.find('am') == -1) and (thisTime.find('pm') == -1)):
			thisTime = thisTime[:-2]


		toJSON.append({
						'website': 'https://www.ecdi.org/events/akron',
						'title' : title[i],
						'location' : 'Akron',
						'description' : description[i],
						'date' : helperFunctions.monthToNum(thisDate[thisDate.find(',') + 2 : thisDate.find(',') + 5]) + "-" + thisDate[thisDate.find(' ', thisDate.find(' ') + 1) + 1 : thisDate.find(' ', thisDate.find(' ') + 1) + 3], 
						'time' : thisTime
					 })
		
	return json.dumps(toJSON)

def getJSONCleveland():
	page = urllib2.urlopen('https://www.ecdi.org/events/cleveland')
	soup = BeautifulSoup(page, "html.parser")
	event = soup.find_all("div", {'class' : 'row class-listing'})

	title = []
	description = []
	date = []
	toJSON = []

	for getEvent in event:
		title.append(getEvent.div.h4.get_text())
		date.append(getEvent.p.em.get_text())
		description.append(getEvent.p.next_sibling.next_sibling.get_text())

	for i in range(len(title)):
		thisDate = date[i]
		thisTime = thisDate[thisDate.find(':') - 2 : thisDate.find(':') + 6].lower()
		if(thisTime[0] == ' '):
			thisTime = thisTime[1:]
		if(thisTime[4] == ' '):
			thisTime = thisTime[:4] + thisTime[5:]
		if(thisTime[5] == ' '):
			thisTime = thisTime[:5] + thisTime[6:]
		if((thisTime.find('am') == -1) and (thisTime.find('pm') == -1)):
			thisTime = thisTime[:-2]


		toJSON.append({
						'website': 'https://www.ecdi.org/events/cleveland',
						'title' : title[i],
						'location' : 'Cleveland',
						'description' : description[i],
						'date' : helperFunctions.monthToNum(thisDate[thisDate.find(',') + 2 : thisDate.find(',') + 5]) + "-" + thisDate[thisDate.find(' ', thisDate.find(' ') + 1) + 1 : thisDate.find(' ', thisDate.find(' ') + 1) + 3], 
						'time' : thisTime
					 })
		
	return json.dumps(toJSON)

def getJSONColumbus():
	page = urllib2.urlopen('https://www.ecdi.org/events/columbus')
	soup = BeautifulSoup(page, "html.parser")
	event = soup.find_all("div", {'class' : 'row class-listing'})

	title = []
	description = []
	date = []
	toJSON = []

	for getEvent in event:
		title.append(getEvent.div.h4.get_text())
		date.append(getEvent.p.em.get_text())
		description.append(getEvent.p.next_sibling.next_sibling.get_text())

	for i in range(len(title)):
		thisDate = date[i]
		thisTime = thisDate[thisDate.find(':') - 2 : thisDate.find(':') + 6].lower()
		if(thisTime[0] == ' '):
			thisTime = thisTime[1:]
		if(thisTime[4] == ' '):
			thisTime = thisTime[:4] + thisTime[5:]
		if(thisTime[5] == ' '):
			thisTime = thisTime[:5] + thisTime[6:]
		if((thisTime.find('am') == -1) and (thisTime.find('pm') == -1)):
			thisTime = thisTime[:-2]


		toJSON.append({
						'website': 'https://www.ecdi.org/events/columbus',
						'title' : title[i],
						'location' : 'Columbus',
						'description' : description[i],
						'date' : helperFunctions.monthToNum(thisDate[thisDate.find(',') + 2 : thisDate.find(',') + 5]) + "-" + thisDate[thisDate.find(' ', thisDate.find(' ') + 1) + 1 : thisDate.find(' ', thisDate.find(' ') + 1) + 3], 
						'time' : thisTime
					 })
		
	return json.dumps(toJSON)

def getJSONToledo():
	page = urllib2.urlopen('https://www.ecdi.org/events/toledo')
	soup = BeautifulSoup(page, "html.parser")
	event = soup.find_all("div", {'class' : 'row class-listing'})

	title = []
	description = []
	date = []
	toJSON = []

	for getEvent in event:
		title.append(getEvent.div.h4.get_text())
		date.append(getEvent.p.em.get_text())
		description.append(getEvent.p.next_sibling.next_sibling.get_text())

	for i in range(len(title)):
		thisDate = date[i]
		thisTime = thisDate[thisDate.find(':') - 2 : thisDate.find(':') + 6].lower()
		if(thisTime[0] == ' '):
			thisTime = thisTime[1:]
		if(thisTime[4] == ' '):
			thisTime = thisTime[:4] + thisTime[5:]
		if(thisTime[5] == ' '):
			thisTime = thisTime[:5] + thisTime[6:]
		if((thisTime.find('am') == -1) and (thisTime.find('pm') == -1)):
			thisTime = thisTime[:-2]


		toJSON.append({
						'website': 'https://www.ecdi.org/events/toledo',
						'title' : title[i],
						'location' : 'Toledo',
						'description' : description[i],
						'date' : helperFunctions.monthToNum(thisDate[thisDate.find(',') + 2 : thisDate.find(',') + 5]) + "-" + thisDate[thisDate.find(' ', thisDate.find(' ') + 1) + 1 : thisDate.find(' ', thisDate.find(' ') + 1) + 3], 
						'time' : thisTime
					 })
		
	return json.dumps(toJSON)