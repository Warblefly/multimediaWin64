### The Deutche Welle channel changes its FLV 
### URL at least once a day.
### This Python program seeks the current URL, and passes it as
### an argument to the chosen media player.
###
### It is a three-part process:
### 1. Ask the server for the link that gives the URLS
### 2. Parse the XML that is returned for the correct RTMP URL
### 3. Feed the RTMP URL to our player

import xml.etree.ElementTree as etree
from xml.sax.saxutils import escape
import urllib.request, urllib.parse, json, ctypes, subprocess


### Alter these variables to suit what you want. You might wish to use
### a different player.

DW_PLAYER="mpv.exe"
DW_PLAYER_OPTIONS="--vf=lavfi=[pp=ac],format=primaries=bt.601-625,unsharp=3:3:0.8 -"
RTMP_COMMAND="rtmpdump.exe"
RTMP_OPTIONS='--live -r %s -y "%s"'
DW_PAGE="http://www.metafilegenerator.de/DWelle/tv-asia/flv/tv.smil"


### Prepare the query
first_query = urllib.request.Request(DW_PAGE)

### Ask for the response
response = urllib.request.urlopen(first_query)
the_response = response.read().decode('utf-8').replace('&', '&amp;')
print(the_response)

### From the response, we want the URL and parameters for
### our second query to a server to return the program video stream

tree = etree.fromstring(the_response)

### In here, we'll need the <video> tag with bandwidth set to "highest"
### So here is a dictionary with src being the playpath, and bandwidth
### being the indicator of bandwidth
### The notation is XPath, defined by W3C.org
### In the dictionary, we extract the value with key 'src'
### Likewise, find the rtmp server, which is the first value with
### key 'base'

playpath=tree.findall('.//video[@bandwidth="highest"]')[0].attrib['src']
rtmp_server=tree.findall('.//meta[@base]')[0].attrib['base']
#print(playpath)
#print(rtmp_server)

### Now we have everything needed for calling the player

command = "cmd.exe /C " + RTMP_COMMAND + " " \
          + RTMP_OPTIONS % (rtmp_server, playpath) \
          + " | mpv --vf=lavfi=[pp=ac],scale=1024:576,unsharp=3:3:0.8 -"

print (command)

subprocess.call(command)

### Program exits after subprocess returns i.e. media player is closed
