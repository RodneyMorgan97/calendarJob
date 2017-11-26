import json
import akronSBDC
import akronSCORE
import ohioMeansJobs
import ecdi
import greaterAkronCoC
import glide
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
from flask import Flask
app = Flask(__name__)

fullJSON = []

@app.route('/update_calendar')
def update_calendar():
	
	akronSBDC_ = akronSBDC.getJSON()
	akronSCORE_ = akronSCORE.getJSON()	
	ohioMeansJobs_ = ohioMeansJobs.getJSON()
	ecdiAkron_ = ecdi.getJSONAkron()
	ecdiCleveland_ = ecdi.getJSONCleveland()
	greaterAkronCoC_ = greaterAkronCoC.getJSON()
	glide_ = glide.getJSON()
	jumpstart_ = jumpstart.getJSON()
	launchNET_ = launchNET.getJSON()
	ksuCCPD_ = ksuCCPD.getJSON()
	glyphixStudio_ = glyphixStudio.getJSON()
	magnet_ = magnet.getJSON()
	aCloserLook_ = aCloserLook.getJSON() #ask about commenting this one out
	noche_ = noche.getJSON()
	akronWomenInTech_ = akronWomenInTech.getJSON()
	womensNetworkNEO_ = womensNetworkNEO.getJSON()
	

	fullJSON = filterJSON(akronSBDC_, akronSCORE_,ohioMeansJobs_,ecdiAkron_, ecdiCleveland_, greaterAkronCoC_, glide_, jumpstart_, launchNET_, ksuCCPD_, glyphixStudio_, magnet_, aCloserLook_, noche_, akronWomenInTech_, womensNetworkNEO_)

	with open('calendarJSON.json', 'w') as outfile:
		json.dump(fullJSON, outfile)

	return 'Updated'

@app.route('/get_calendar')
def get_calendar():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "calendarJSON.json")
	data = jsonify(json.load(open(json_url)))
	return data

def filterJSON(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen):
	filteredJSON = []

	if (one):
		filteredJSON.append(one)

	if (two):
		filteredJSON.append(two)

	if (three):
		filteredJSON.append(three)

	if (four):
		filteredJSON.append(four)

	if (five):
		filteredJSON.append(five)

	if (six):
		filteredJSON.append(six)

	if (seven):
		filteredJSON.append(seven)

	if (eight):
		filteredJSON.append(eight)

	if (nine):
		filteredJSON.append(nine)

	if (ten):
		filteredJSON.append(ten)

	if (eleven):
		filteredJSON.append(eleven)

	if (twelve):
		filteredJSON.append(twelve)

	if (thirteen):
		filteredJSON.append(thirteen)

	if (fourteen):
		filteredJSON.append(fourteen)

	if (fifteen):
		filteredJSON.append(fifteen)

	if (sixteen):
		filteredJSON.append(sixteen)

	return filteredJSON


