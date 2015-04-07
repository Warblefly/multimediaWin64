### The Euronews 24-hour EBU news channel changes its playlist
### URL at least once a day.
### This Python program seeks the current URL, and passes it as
### an argument to the chosen media player.
###
### It is a three-part process:
### 1. Ask the server for the link that gives the URLS
### 2. Ask the link for its JSON list of URLS containing the chunked playlists
### 3. Choose from the JSON list the URL for high-quality English

import urllib.request, urllib.parse, json, ctypes, subprocess


### Alter these variables to suit what you want. You might wish to use
### a different player.

EN_PLAYER="mpv.exe"
EN_PLAYER_OPTIONS="--vf=lavfi=[pp=ac],format=primaries=bt.601-625,unsharp=3:3:0.8"
EN_PAGE="http://www.euronews.com/news/streaming-live/"
EN_QUERY={'action': 'getHexaglobeUrl'}

### We must use a POST request to ask for the link to the JSON list.
### GET does not work.

### Prepare the query
data = urllib.parse.urlencode(EN_QUERY)
data = data.encode('utf-8')
first_query = urllib.request.Request(EN_PAGE, data)

### Ask for the response
response = urllib.request.urlopen(first_query)
the_response = response.read()

### From the response, we want the parts that will make up
### our second query to a server to get the programme URLs

parts = urllib.parse.urlparse(the_response).decode()

protocol, server, filename, second_query = \
          parts[0], parts[1], parts[2], parts[4]

### Deconstruct the second query

second_query_tuple = urllib.parse.parse_qsl(second_query)

### As before, use these variables to make a new query to another
### server, which this time returns a JSON response

url = protocol + "://" + server + filename

data = urllib.parse.urlencode(second_query_tuple)
full_url = url + '?' + data

response = urllib.request.urlopen(full_url)
the_response = response.read().decode()

decoded = json.loads(the_response)

euronews_URL = decoded["primary"]["en"]["hls"]

subprocess.call("%s %s %s" % (EN_PLAYER, EN_PLAYER_OPTIONS, euronews_URL))

### Program exits after subprocess returns i.e. media player is closed
