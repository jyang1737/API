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

#L = ['no person','pyrite','love','christmas','hack','day']
# returns the top valid tag
def query(L):
    n = 0
    while(n<len(L)):
        if(L[n]=="no person"):
            n+=1
        else:
            p = urllib2.urlopen(request(L[n])).read()
            d1 = json.loads(p)
            d2 = d1['message']['body']['track_list']
            #print len(d2)
            if(len(d2)<10):
                n+=1
            else:
                return L[n]
    if (L[0]=="no person"):
        return L[1]
    else:
        return L[0]
#print query(L)

# parse json
# takes a list of tags, returns a list of track ids
def get_tracks(tags):
    p = urllib2.urlopen(request(query(tags))).read()
    d1 = json.loads(p)
    d2 = d1['message']['body']['track_list']#[n]['track']
    d2 = sorted(d2, key=lambda k: k['track']['track_rating'])#['num_favourite'])
    tracks = []
    n = len(d2)-1
    end = n-10
    while (n >= 0 and n >= end):
        tracks.append(d2[n]['track']['track_id'])
        n-=1
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
    return d
#print get_title(15953433)

#for i in get_tracks(["gargantuan","hhfkjhg","pyrite"]):
#    print get_title(i)

def get_artist(id):
    u = "http://api.musixmatch.com/ws/1.1/track.get?apikey="+api()
    r = urllib2.Request(u+'&track_id='+str(id))#,data=None)
    p = urllib2.urlopen(r).read()
    d = json.loads(p)
    d = d['message']['body']['track']['artist_name']
    return d
#print get_artist(15953433)    


'''
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
    if (len(L)>0):
        if(L[0]=="no person"):
            return L[1]
        return L[0]
    else:
        return False

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

# returns song lyrics
def lyrics(L):
    if(query(L)==False):
        return "A song could not be found."
    else:
        song = get_id(query(L))
        m = get_lyrics(song[0])
        return m
#print lyrics(L)

# returns song artist
def get_artist(L):
    song = get_id(query(L))
    m = song[2]
    return m

# returns song title
def get_title(L):
    song = get_id(query(L))
    m = song[1]
    return m

#https://developer.musixmatch.com/documentation/rights-clearance-on-your-existing-catalog
#https://developer.musixmatch.com/documentation/api-reference/tracking-url-get
'''

