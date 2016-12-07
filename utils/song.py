#!/usr/bin/env python

import json

import urllib2,urllib


url="http://api.musixmatch.com/ws/1.1/tracking.url.get?apikey=5f423b7772a80f77438407c8b78ff305&format=json"

#class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])


# search for song
#track.search?q_track=back%20to%20december&q_artist=taylor%20swift&f_has_lyrics=1
#track.search?q_lyrics=music%20hack%20day

def get_song(L):
    s = "track.search?q_lyrics="
    n = 0
    while n < len(L):
        s += L[n]
        if n < (len(L) - 1):
            s += "%20"
        n += 1
    return s

#print get_song(["music","hack","day"])
'''
L = ["music","hack","day"]
req = urllib2.Request('http://api.musixmatch.com/ws/1.1/'+get_song(L))
response = urllib2.urlopen(req)
the_page = response.read()

print the_page
'''

# get lyrics after search is done
#track.lyrics.get?track_id=15953433

# parse json
#https://docs.python.org/2/library/json.html
def get_lyrics():
    urllib2.urlopen(url).read()
    d1 = json.loads(req)
    d2 = {}
    # insert tag stuff

#<img src="http://tracking.musixmatch.com/t1.0/AMa6hJCIEzn1v8RuXW">
#script type="text/javascript" src="http://tracking.musixmatch.com/t1.0/AMa6hJCIEzn1v8RuOP"

# download https://github.com/musixmatch/musixmatch-sdk/blob/master/dist/python-client-generated.zip
# pip install six
# pip install urllib3
# pip install certifi


#https://developer.musixmatch.com/documentation/rights-clearance-on-your-existing-catalog
#https://developer.musixmatch.com/documentation/api-reference/tracking-url-get
