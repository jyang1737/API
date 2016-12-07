import json, urllib2, urllib

def getlist(path):
    key = getkey()
    url = "https://api.clarifai.com/v1/tag/?url="+path+"&access_token="+key
    u = urllib2.urlopen(url)
    r = u.read()
    d = json.loads(r)
    return d['results'][0]['result']['tag']['classes']




def getkey():
    url = "https://api.clarifai.com/v1/token"
    data = urllib.urlencode({"client_id":"GX_1FH8Q7PkZxDcrkTzZ_yCfK-ArAC5wfTgGNUHV", 'client_secret':'jI4F23y0OxOXGg9NQ41-QJJt7xgWUEN2JB93lvNm', "grant_type":"client_credentials"})
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    r = response.read()
    d = json.loads(r)
    return d['access_token']
