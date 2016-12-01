# -*- coding: latin-1 -*-

#Gets TVMaze info for last aired episode info using TVMaze ID

#libraries for json and url
import json, urllib.request, sys
#argument 1 should be tvmaze id
mazeid = sys.argv[1]
#adds strings to variable url
url = "http://api.tvmaze.com/shows/" + mazeid
#reads url, decodes to utf8 char encoding
response = urllib.request.urlopen(url).read().decode('utf-8')
#reads and parses json string to variable parsed_json
parsed_json = json.loads(response)
#gets url for next episode
nextepUrl = parsed_json["_links"]["previousepisode"]["href"];
response = urllib.request.urlopen(nextepUrl).read().decode('utf-8');
parsed_json = json.loads(response);
#Prints the parsed json, at value of passed argument 2, name, airdate etc
print(parsed_json[sys.argv[2]])
