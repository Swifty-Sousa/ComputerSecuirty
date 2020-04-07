#!/usr/bin/python

# Get a super secret secure key from freeaeskey.xyz

import urllib2

resp = urllib2.urlopen('http://freeaeskey.xyz')
data = resp.read()
key = data[data.index('<b>')+3:data.index('</b>')]
print key
