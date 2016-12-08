import json, urllib2, urllib, os, mimetypes, tempfile, httplib

def getlist(path):
    key = getkey()
    url = "https://api.clarifai.com/v1/tag/?url="+path+"&access_token="+key
    data = {"url":path}
    values = urllib.urlencode(data)
    headers = {"Authorization" : "Bearer " + key}
    request = urllib2.Request(url,values,headers = headers)
    u = urllib2.urlopen(request)
    r = u.read()
    d = json.loads(r)
    return d['results'][0]['result']['tag']['classes']

def getlistlocal(path):
    key = getkey()
    url = "https://api.clarifai.com/v1/tag/"
    values={'encoded_data' :"@"+path}
    datagen = urllib.urlencode(values)
    headers = {'Authorization' : 'Bearer ' + key}
    # contnet
    # register_openers()
    # datagen, headers = multipart_encode({"encoded_data": open(path)})
    request = urllib2.Request(url, datagen, headers=headers)
    r = urllib2.urlopen(request)
    q = r.read()
    return q

def getkey():
    url = "https://api.clarifai.com/v1/token"
    data = urllib.urlencode({"client_id":"GX_1FH8Q7PkZxDcrkTzZ_yCfK-ArAC5wfTgGNUHV", 'client_secret':'jI4F23y0OxOXGg9NQ41-QJJt7xgWUEN2JB93lvNm', "grant_type":"client_credentials"})
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    r = response.read()
    d = json.loads(r)
    return d['access_token']


def post_multipart(host, selector, fields, files):
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTP(host)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    return h.file.read()

def encode_multipart_formdata(fields, files):
    LIMIT = '----------lImIt_of_THE_fIle_eW_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + LIMIT)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + LIMIT)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + LIMIT + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % LIMIT
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
