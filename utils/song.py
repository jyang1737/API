#!/usr/bin/env python

import json, urllib, urllib2

apikey="5e77a0cfadb9f7b386968d9150c3d0f2"
url="http://api.musixmatch.com/ws/1.1/track.search?apikey=5e77a0cfadb9f7b386968d9150c3d0f2&format=json"

def request(k):
    return urllib2.Request(url+'&q_lyrics='+k+'&f_has_lyrics=1')#,data=None)
    #return urllib2.Request(url+k+'&f_has_lyrics=1')#,data=None)

#L = ['music','hack','day']
def query(L):
    if(len(L)>4):
        L = L[0:4]
    s = ''
    n = 0
    while n < len(L):
        s += L[n]
        if n < (len(L) - 1):
            s += "%20"
        n += 1
    return s
#print query(L)

# parse json
def get_id(query):
    #p = urllib2.urlopen(request("music%20hack%20day")).read()
    p = urllib2.urlopen(request(query)).read()
    d1 = json.loads(p)
    n = 0 # song number in list of matches
    d2 = d1['message']['body']['track_list'][n]['track']
    name = d2['track_name']
    id = d2['track_id']
    return [id,name]
    #return name
#print get_id(query(L))

# get lyrics after search is done
#track.lyrics.get?track_id=15953433
def get_lyrics(id):
    u = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey=5e77a0cfadb9f7b386968d9150c3d0f2&format=json"
    r = urllib2.Request(u+'&track_id='+str(id))#,data=None)
    p = urllib2.urlopen(r).read()
    d = json.loads(p)
    d = d['message']['body']['lyrics']
    return d['lyrics_body']


def lyrics(L):
    song=get_id(query(L))
    return song[1]+"\n\n"+get_lyrics(song[0])

#print lyrics(L)

#https://developer.musixmatch.com/documentation/rights-clearance-on-your-existing-catalog
#https://developer.musixmatch.com/documentation/api-reference/tracking-url-get
