from urllib.request import urlopen
import urllib.error
import requests


def urlfunc():
    r = urlopen('http://httpbin.org/headers')
    print("urlfunc - type of r : ", type(r)) # <class 'http.client.HTTPResponse'>
    print(r.read().decode('ascii'))

def reqfunc():
    r = requests.get("http://httpbin.org/headers") 
    print("reqfunc - type of r : ", type(r)) # <class 'requests.models.Response'>
    print(r.text)

urlfunc()
reqfunc()