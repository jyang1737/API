import json, urllib2, urllib, os, mimetypes, tempfile, httplib, formdata
from encode import multipart_encode
from streaminghttp import register_openers

def getlist(path):
    key = getkey()
    url = "https://api.clarifai.com/v1/tag/"
    data = {"url":path}
    values = urllib.urlencode(data)
    headers = {"Authorization" : "Bearer " + key}
    request = urllib2.Request(url,values,headers = headers)
    u = urllib2.urlopen(request)
    r = u.read()
    d = json.loads(r)
    return d['results'][0]['result']['tag']['classes']

def getlistcolors(path):
    key = getkey()
    url = "https://api.clarifai.com/v1/color/"
    data = {"url":path}
    values = urllib.urlencode(data)
    headers = {"Authorization" : "Bearer " + key}
    request = urllib2.Request(url,values,headers = headers)
    u = urllib2.urlopen(request)
    r = u.read()
    d = json.loads(r)
    if len(d['results'][0]['colors']) > 1:
        return [d['results'][0]['colors'][0]['w3c']['hex'], d['results'][0]['colors'][1]['w3c']['hex']]
    else:
        return [d['results'][0]['colors'][0]['w3c']['hex']]
def getlistlocal(filename):
    key = getkey()
    register_openers()
    path = "static/" + filename
    url = "https://api.clarifai.com/v1/tag/"
    fields = {}
    f = open(path)
    f2 = f
    fields = {'encoded_data':f}
    data,headers = multipart_encode(fields)
    headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    request = urllib2.Request(url, data=data, headers=headers)
    request.add_header('Authorization','Bearer ' + key)
    request.unverifiable = True
    r = urllib2.urlopen(request)
    q = r.read()
    d = json.loads(q)
    return d['results'][0]['result']['tag']['classes']

def getlistlocalcolors(filename):
    key = getkey()
    register_openers()
    path = "static/" + filename
    url = "https://api.clarifai.com/v1/color/"
    fields = {}
    f = open(path)
    f2 = f
    fields = {'encoded_data':f}
    data,headers = multipart_encode(fields)
    headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    request = urllib2.Request(url, data=data, headers=headers)
    request.add_header('Authorization','Bearer ' + key)
    request.unverifiable = True
    r = urllib2.urlopen(request)
    q = r.read()
    d = json.loads(q)
    if len(d['results'][0]['colors']) > 1:
        return [d['results'][0]['colors'][0]['w3c']['hex'], d['results'][0]['colors'][1]['w3c']['hex']]
    else:
        return [d['results'][0]['colors'][0]['w3c']['hex']]


def getkey():
    f = open('secretdata.txt', 'r')
    lines = f.readlines()
    iid = lines[0].strip('\n')
    secret = lines[1].strip('\n')
    url = "https://api.clarifai.com/v1/token"
    data = urllib.urlencode({"client_id":iid, 'client_secret':secret, "grant_type":"client_credentials"})
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    r = response.read()
    d = json.loads(r)
    return d['access_token']

