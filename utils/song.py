#!/usr/bin/env python

import json, urllib, urllib2

def api():
    file = open("secretdata.txt",'r')
    m = file.readline()
    m = file.readline()
    m = file.readline()
    return m[0:-1]
#print api()
url="http://api.musixmatch.com/ws/1.1/track.search?apikey="+api()+"&format=json"

def request(k):
    return urllib2.Request(url+'&q_lyrics='+k+'&f_has_lyrics=1')

#L = ['christmas','hack','day']
def query(L):
    #if(len(L)>4):
    #    L = L[0:4]
    #s = ''
    #n = 0
    #while n < len(L):
    #    s += L[n]
    #    if n < (len(L) - 1):
    #        s += "%20"
    #    n += 1
    #return s
    if (len(L)>0):
        return L[0]
    else:
        return False
#print query(L)

# parse json
def get_id(query):
    p = urllib2.urlopen(request(query)).read()
    d1 = json.loads(p)
    #n = 0 # song number in list of matches
    d2 = d1['message']['body']['track_list']#[n]['track']
    d2 = sorted(d2, key=lambda k: k['track']['track_rating'])#['num_favourite'])
    n = len(d2)-1
    d2 = d2[n]['track']
    #print d2
    rating = d2['track_rating']
    name = d2['track_name']
    id = d2['track_id']
    artist = d2['artist_name']
    coverart = d2['album_coverart_100x100']
    #print name+str(id)+artist+coverart+str(rating)
    return [id,name,artist,coverart]
    #return name
#print get_id(query(L))

# get lyrics after search is done
#track.lyrics.get?track_id=15953433
def get_lyrics(id):
    u = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey="+api()
    r = urllib2.Request(u+'&track_id='+str(id))#,data=None)
    p = urllib2.urlopen(r).read()
    d = json.loads(p)
    d = d['message']['body']['lyrics']
    return d['lyrics_body']

# returns a string of lyrics for 30% of the matched song
'''
def lyrics(L):
    if(query(L)==False):
        return "A song could not be found."
    else:
        song=get_id(query(L))
        m = song[1]+"\n\n"+get_lyrics(song[0])
        return m
'''

# returns a list of matched song attributes [title, artist, lyrics, coverart]
def lyrics(L):
    if(query(L)==False):
        return "A song could not be found."
    else:
        song=get_id(query(L))
        m = song[1]+"\n\n"+get_lyrics(song[0])
        return m
#print lyrics(L)

#https://developer.musixmatch.com/documentation/rights-clearance-on-your-existing-catalog
#https://developer.musixmatch.com/documentation/api-reference/tracking-url-get
