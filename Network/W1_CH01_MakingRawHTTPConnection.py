# 1주차 강의교안의 22페이지 내용
import http.client
import json  # JSON
from urllib.parse import quote_plus  # Parse URLs into components

base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = 'David'
    headers = {'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)  # GET Request
    print(path, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply[0]['lat'], reply[0]['lon'])


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
