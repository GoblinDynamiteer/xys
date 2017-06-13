# -*- coding: latin-1 -*-

#Gets OMDB info using IMDB-id

#libraries for json and url
import json, urllib.request, sys
#argument 1 should be imdb-id
title = sys.argv[1]
year = sys.argv[2]
#adds strings to variable url
url = "http://www.omdbapi.com/?apikey=#####&t=" + title + "&y=" + year + "&plot=short&r=json"
#reads url, decodes to utf8 char encoding
response = urllib.request.urlopen(url).read().decode('utf-8')
#reads and parses json string to variable parsed_json
parsed_json = json.loads(response)
#Prints the parsed json, at value of passed argument 2 (can be title, year, etc for this case)
print(parsed_json["Title"] + "|" + parsed_json["Year"] + "|" + parsed_json["Genre"] + "|" + parsed_json["imdbID"])
