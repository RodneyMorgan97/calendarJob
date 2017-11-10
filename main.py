import json

import akronSBDC
import akronSCORE
import codeAkronFacebook
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
import neotec
import ODSA
import aCloserLook
import noche
import iCorps
import akronWomenInTech
import womensNetworkNEO

fullJSON = []
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
fullJSON.append(ODSA.getJSON())
fullJSON.append(aCloserLook.getJSON())
fullJSON.append(noche.getJSON())
fullJSON.append(akronWomenInTech.getJSON())
fullJSON.append(womensNetworkNEO.getJSON())
print json.dumps(fullJSON)



#print codeAkronFacebook.getJSON() #TBD
#print iCorps.getJSON() #shouldn't be on list
#print neotec.getJSON() #still needs done