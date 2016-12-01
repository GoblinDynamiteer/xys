# -*- coding: latin-1 -*-

#Gets OMDB info using IMDB-id

#libraries for json and url
import json, urllib.request, sys
#argument 1 should be imdb-id
imdb = sys.argv[1]
#adds strings to variable url
url = "http://www.omdbapi.com/?i=" + imdb + "&y=&plot=short&r=json"
#reads url, decodes to utf8 char encoding
response = urllib.request.urlopen(url).read().decode('utf-8') 
#reads and parses json string to variable parsed_json
parsed_json = json.loads(response)
#Prints the parsed json, at value of passed argument 2 (can be title, year, etc for this case)
print(parsed_json[sys.argv[2]]) 
