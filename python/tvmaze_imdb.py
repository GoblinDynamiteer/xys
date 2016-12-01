# -*- coding: latin-1 -*-

#Gets TVMaze info using IMDB-id

#libraries for json and url
import json, urllib.request, sys
#argument 1 should be imdb-id
imdb = sys.argv[1]
#adds strings to variable url
url = "http://api.tvmaze.com/lookup/shows?imdb=" + imdb
#reads url, decodes to utf8 char encoding
response = urllib.request.urlopen(url).read().decode('utf-8')
#reads and parses json string to variable parsed_json
parsed_json = json.loads(response) 
#Prints the parsed json, at value of passed argument 2, id, name etc
print(parsed_json[sys.argv[2]])
