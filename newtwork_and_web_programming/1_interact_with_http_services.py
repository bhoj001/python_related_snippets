"""
purpose: To learn about network and web programming in python.This tutorial
is from david beazley book. Chapter 11.

Topic: making a request in HTTp resources (get and post example)

date: 2020/July/24th
author:Bhoj bahadur karki
Motivation: To be able to build my own server.
Quote: Those who believe can, will do it.


Problem: Interact with HTTP Services as a Client
Approach: use builtin urllib libaray
"""

from urllib import request, parse

url = "https://httpbin.org/get"

params ={
    "name1":'value1',
    "name2":"value2"
}
querystring = parse.urlencode(params)

u = request.urlopen(url+"?"+querystring)

resp = u.read()
print(resp)


# performing post request with header data.
# header data is optional to sent but sometime we need to send header data

url = "https://httpbin.org/post"

# Extra headers
headers = {
    "User-agent":"none/ofyourbusiness",
    "Spam": 'Eggs'
}


req = request.Request(url, querystring.encode('ascii'), headers=headers)

# make a request and read the response

u = request.urlopen(req)
data = u.read()

# print receive data to file
with open("randomfile.txt","wb") as f:
    f.write(data)



print(data)
