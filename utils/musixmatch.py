#!/usr/bin/env python

#
# Musixmatch Python API client
# @author Loreto Parisi (loreto at musixmatch dot com)
# @see https://developer.musixmatch.com/documentation
# @copy 2016 Musixmatch Spa


import six
import urllib2
import urllib3



import time
import sys

import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

url="http://api.musixmatch.com/ws/1.1/tracking.url.get?apikey=5f423b7772a80f77438407c8b78ff305&format=json"
endurl="http://api.musixmatch.com/ws/1.1/"



req = urllib2.Request(url+'track.search?q_lyrics=music%20hack%20day')#,data=None)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page


if len(sys.argv) <= 1:
    print "\nUsage: python musixmatch.py 5e77a0cfadb9f7b386968d9150c3d0f2";
    exit();

# str | Account api key, to be used in every api call
swagger_client.configuration.api_key['apikey'] = sys.argv[1]

# create an instance of the API class
api_instance = swagger_client.AlbumApi()
album_id = '14250417' # str | The musiXmatch album id
format = 'json' # str | output format: json, jsonp, xml. (optional) (default to json)

try:
    # 
    api_response = api_instance.album_get_get(album_id, format=format)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->album_get_get: %s\n" % e

