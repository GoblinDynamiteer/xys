# -*- coding: latin-1 -*-

#Handles UNC JSON response
import json, urllib.request, sys
url = sys.argv[1]

jsonResponse = urllib.request.urlopen(url).read().decode('utf-8')
decodedJson = json.loads(jsonResponse) 

#returned several search hits
if isinstance(decodedJson["channel"]["item"], list):
	numberItems = len(decodedJson["channel"]["item"])
	for n in range(0,numberItems):
		print(decodedJson["channel"]["item"][n]["title"], ";", decodedJson["channel"]["item"][n]["link"])
		if n != numberItems:
			print("|") #for list separator in xyplorer script

#returned only one search hit
elif  isinstance(decodedJson["channel"]["item"], dict):
	print(decodedJson["channel"]["item"]["title"], ";", decodedJson["channel"]["item"]["link"])


