### WDIO's HD on-line stream changes its authorization parameters
### quite often, understandably. It also requires cookies for
### authentication.
###
### This Python program seeks the current chunked playlist, and passes it as
### an argument to the chosen media player.
###
### It is a multi-part process:
### First, retrieve the chunked playlist (m3u8) URL
### from http://livestream.com/accounts/12241516/events/3818871/player
### This is a large chunk of javascript, but we need only minimally
### parse it, for the value assigned to "m3u8_url"
### We then request that URL, storing both the response, and
### the cookies. The cookies are for authentication in the following
### step.

import urllib.request, urllib.parse, json, ctypes, subprocess, re
import http.cookiejar


### Alter these variables to suit what you want. You might wish to use
### a different player.

WDIO_PLAYER = "mpv.exe"
WDIO_PLAYER_OPTIONS = "--no-ytdl --hwdec=auto --vd-lavc-fast --vd-lavc-skiploopfilter=nonref"
WDIO_LIVESTREAM_PLAYER_CONFIG = \
    "http://livestream.com/accounts/12241516/events/3818871/player"

### Python backslashes need escaping
WDIO_STREAM_REGEX = '(\\"m3u8_url\\":\\")(.*?)(\\",\\"?)'.encode()

### First get the page with the current link

first_query = urllib.request.Request(WDIO_LIVESTREAM_PLAYER_CONFIG)
first_response = urllib.request.urlopen(first_query).read()

### Group 2 is the second group in the regex, the URL we want.

first_match = re.search(WDIO_STREAM_REGEX, first_response).group(2).decode()

second_cookies = urllib.request.HTTPCookieProcessor()
second_query = urllib.request.Request(first_match)
second_response = urllib.request.urlopen(second_query).read()

### In the second_response string, we get the proper URLs for display.

subprocess.call("%s %s %s" % (WDIO_PLAYER, WDIO_PLAYER_OPTIONS, first_match))

### Program exits after subprocess returns i.e. media player is closed
