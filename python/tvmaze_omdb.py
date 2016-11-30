# -*- coding: latin-1 -*-

#Searches OMDb for json-respones, where title is passed argument 1, and returns value at argument 2

import json, urllib.request, sys #libraries for json and url
#sys.argv[0] contains script-name -- similar to C
#sys.argv[1] contains passed argument 1 -- similar to C
#sys.argv[2] contains passed argument 2
#sys.argv[3] contains passed argument 3  1 = OMDb 2= TVmaze

imdb = sys.argv[1]

#http://www.omdbapi.com/?t=hannibal&y=&plot=short&r=json
if int(sys.argv[2]) == 1: #Arguments are passed as strings? Use int() to convert to integer
	url = "http://www.omdbapi.com/?i=" + imdb + "&y=&plot=short&r=json" #adds strings to variable url

elif int(sys.argv[2]) == 2:
	url = "http://api.tvmaze.com/lookup/shows?imdb=" + imdb
	
else:
	print("Wrong arg2")

response = urllib.request.urlopen(url).read().decode('utf-8') #reads url, decodes to utf8 char encoding
parsed_json = json.loads(response) #reads and parses json string to variable parsed_json

if sys.argv[3] == "lastAired":
	#print(parsed_json["_links"]["previousepisode"]["href"])
	lastepUrl = parsed_json["_links"]["previousepisode"]["href"];
	response = urllib.request.urlopen(lastepUrl).read().decode('utf-8');
	parsed_json = json.loads(response);
	print(parsed_json[sys.argv[4]]);

else:
	print(parsed_json[sys.argv[3]]) #Prints the parsed json, at value of passed argument 2 (can be title, year, etc for this case)

#xyplorer test: 
#echo runret('python json_web_argv.py "the terminator" "Year"', "D:\Google Drive\Utbildning\Mjukvaruutvecklare inbyggda system\Kod\Python\Testing\JSON\");
#Will get 'year' of movie 'the terminator'
#python json_tvmaze_omdb.py tt0475784 2 lastAired
