import json

import akronSBDC
import akronSCORE
import ohioMeansJobs
import ecdi
import greaterAkronCoC
import glide
import goodwill
import jumpstart
import launchNET
import ksuCCPD
import glyphixStudio
import magnet
import aCloserLook
import noche
import akronWomenInTech
import womensNetworkNEO
import os
from flask import jsonify

fullJSON = []


from flask import Flask
app = Flask(__name__)

@app.route('/get_calendar')
def get_calendar():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "calendarJSON.json")
	data = jsonify(json.load(open(json_url)))
	return data
	

@app.route('/update_calendar')
def update_calendar():
	fullJSON.append(akronSBDC.getJSON())
	fullJSON.append(akronSCORE.getJSON())
	fullJSON.append(ohioMeansJobs.getJSON())
	fullJSON.append(ecdi.getJSONAkron())
	fullJSON.append(ecdi.getJSONColumbus())
	fullJSON.append(ecdi.getJSONCleveland())
	fullJSON.append(ecdi.getJSONToledo())
	fullJSON.append(goodwill.getJSON())
	fullJSON.append(greaterAkronCoC.getJSON())
	fullJSON.append(glide.getJSON())
	fullJSON.append(jumpstart.getJSON())
	fullJSON.append(launchNET.getJSON())
	fullJSON.append(ksuCCPD.getJSON())
	fullJSON.append(glyphixStudio.getJSON())
	fullJSON.append(magnet.getJSON())
	fullJSON.append(aCloserLook.getJSON())
	fullJSON.append(noche.getJSON())
	fullJSON.append(akronWomenInTech.getJSON())
	fullJSON.append(womensNetworkNEO.getJSON())
	with open('calendarJSON.json', 'w') as outfile:
		json.dump(fullJSON, outfile)

	return 'calendar has been updated'


#print codeAkronFacebook.getJSON() #TBD
#print iCorps.getJSON() #shouldn't be on list
#print neotec.getJSON() #still needs done
# fullJSON.append(ODSA.getJSON())