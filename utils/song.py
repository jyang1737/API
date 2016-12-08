#!/usr/bin/env python

import json, urllib, urllib2

apikey="5e77a0cfadb9f7b386968d9150c3d0f2"
url="http://api.musixmatch.com/ws/1.1/track.search?apikey=5e77a0cfadb9f7b386968d9150c3d0f2&format=json"

def request(k):
    return urllib2.Request(url+'&q_lyrics='+k+'&f_has_lyrics=1')#,data=None)
    #return urllib2.Request(url+k+'&f_has_lyrics=1')#,data=None)

L = ['music','hack','day']
def query(L):
    s = ''
    n = 0
    while n < len(L):
        s += L[n]
        if n < (len(L) - 1):
            s += "%20"
        n += 1
    return s

print query(L)

# parse json
#https://docs.python.org/2/library/json.html
def get_id(query):
    #p = urllib2.urlopen(request("music%20hack%20day")).read()
    p = urllib2.urlopen(request(query)).read()
    d1 = json.loads(p)
    n = 0 # song number in list of matches
    d2 = d1['message']['body']['track_list'][n]['track']
    name = d2['track_name']
    id = d2['track_id']
    #return id
    return name
    
print get_id(query(L))

'''
k = "music%20hack%20day"
#req = urllib2.Request(url+'track.search?q_lyrics='+k+'&f_has_lyrics=1')#,data=None)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
'''

#class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])


# search for song
#track.search?q_track=back%20to%20december&q_artist=taylor%20swift&f_has_lyrics=1
#track.search?q_lyrics=music%20hack%20day

def get_song(L):
    s = "track.search?q_lyrics="

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



#<img src="http://tracking.musixmatch.com/t1.0/AMa6hJCIEzn1v8RuXW">
#script type="text/javascript" src="http://tracking.musixmatch.com/t1.0/AMa6hJCIEzn1v8RuOP"

# download https://github.com/musixmatch/musixmatch-sdk/blob/master/dist/python-client-generated.zip
# pip install six
# pip install urllib3
# pip install certifi


#https://developer.musixmatch.com/documentation/rights-clearance-on-your-existing-catalog
#https://developer.musixmatch.com/documentation/api-reference/tracking-url-get
