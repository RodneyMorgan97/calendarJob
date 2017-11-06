#Second Source
from bs4 import BeautifulSoup
import urllib2
import json
import helperFunctions

def getJSON():
	page = urllib2.urlopen('https://akron.score.org/content/take-workshop-282')
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find_all("h4", {'class' : 'content-block__title'}) #string.strip
	location = soup.find_all("span", {'itemprop' : 'streetAddress'}) #string.strip
	description = soup.find_all("div", {'itemprop' : 'description'}) #get_text
	date = soup.find_all("div", {'class' : 'content-block__extra content-block__event-date'})

	toJSON = []


	for i in range(len(title)):

		dateAndTime = date[i].string.strip()
		calendarDate = dateAndTime[0:dateAndTime.find(',', dateAndTime.find(',') + 1)]
		time = dateAndTime[dateAndTime.find(',', dateAndTime.find(',') + 1) + 1 : - 4]
		toJSON.append({
						'website': 'https://akron.score.org/content/take-workshop-282',
						'title' : title[i].string.strip(),
						'location' : location[i].string.strip(),
						'description' : description[i].get_text(),
						'date' : helperFunctions.monthToNum(calendarDate[0:calendarDate.find(" "):]) + "-" + calendarDate[calendarDate.find(" ") + 1 : calendarDate.find(",")],
						'time' : time
					  })
	return json.dumps(toJSON)