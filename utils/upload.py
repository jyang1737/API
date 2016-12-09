import json, urllib2, urllib, os, mimetypes, tempfile, httplib, formdata

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
    return [d['results'][0]['colors'][0]['w3c']['hex'], d['results'][0]['colors'][1]['w3c']['hex']]

def getlistlocal(path,filename):
    key = getkey()
    url = "https://api.clarifai.com/v1/tag/"
    fields = {}
    f = open(path,'r')
    f2 = f.read()
    files= {'encoded_data':{'filename': filename, 'content' :f2}}
    print files
    data, headers = formdata.encode_multipart(fields,files)
    # contnet
    # register_openers()
    request = urllib2.Request(url, data=data, headers=headers)
    request.add_header('Authorization','Bearer ' + key)
    r = urllib2.urlopen(request)
    q = r.read()
    return q

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

