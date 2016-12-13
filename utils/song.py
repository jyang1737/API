#!/usr/bin/env python

import json, urllib, urllib2

def api():
    file = open("secretdata.txt",'r')
    m = file.readline()
    m = file.readline()
    m = file.readline()
    return m[0:-1]

url="http://api.musixmatch.com/ws/1.1/track.search?apikey="+api()+"&format=json"

def request(k):
    return urllib2.Request(url+'&q_lyrics='+k+'&f_has_lyrics=1')

def load_tracks(query):
    p = urllib2.urlopen(request(query)).read()
    d1 = json.loads(p)
    d2 = d1['message']['body']['track_list']
    d2 = sorted(d2, key=lambda k: k['track']['track_rating'])
    return d2

# takes a list of tags, returns a list of track ids
def get_tracks(tags):
    tracks = []
    n = 0
    while(len(tracks) < 10 and n < len(tags)):
        if(tags[n]=="no person" or tags[n]=="boy"):
            n += 1
        elif(n < len(tags)-1):
            d2 = load_tracks(tags[n]+"%20"+tags[n+1])
            m = len(d2) - 1
            end = m - 10
            while (m >= 0 and m >= end and len(tracks) < 10):
                tracks.append(d2[m]['track']['track_id'])
                m -= 1
        if (len(tracks) < 10):
            d2 = load_tracks(tags[n])
            m = len(d2) - 1
            end = m - 10
            while (m >= 0 and m >= end and len(tracks) < 10):
                tracks.append(d2[m]['track']['track_id'])
                m -= 1
        n += 1
    return tracks
    
# get lyrics after search is done
def get_lyrics(id):
    u = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey="+api()
    r = urllib2.Request(u+'&track_id='+str(id))#,data=None)
    p = urllib2.urlopen(r).read()
    d = json.loads(p)
    d = d['message']['body']['lyrics']
    return d['lyrics_body']

def get_title(id):
    u = "http://api.musixmatch.com/ws/1.1/track.get?apikey="+api()
    r = urllib2.Request(u+'&track_id='+str(id))#,data=None)
    p = urllib2.urlopen(r).read()
    d = json.loads(p)
    d = d['message']['body']['track']['track_name']
    if "\u200b" in d:
        d = d[0:-6]
    return d

def get_artist(id):
    u = "http://api.musixmatch.com/ws/1.1/track.get?apikey="+api()
    r = urllib2.Request(u+'&track_id='+str(id))#,data=None)
    p = urllib2.urlopen(r).read()
    d = json.loads(p)
    d = d['message']['body']['track']['artist_name']
    return d
