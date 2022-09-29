import csv
import os
from wsgiref.simple_server import make_server
import requests
from pprint import pformat

def init():
    global dict
    dict = {}
    path = os.path.dirname(__file__)
    f = open(path+"/problem1_csv.csv", 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        dict[ line[0] ] = line[1] 
    # read complete

def app(environ, start_response):
    host = environ.get("HTTP_POST", '127.0.0.1')
    path = environ.get('PATH_INFO', '/')

    if ':' in host:
        host, port = host.split(':', 1)
    if '?' in path:
        path, query = path.split('?', 1)
    headers = [ ('Content-Type', 'text/plain; charset=utf-8') ]
    if environ['REQUEST_METHOD'] != 'GET':
        start_response('501 Not Implemented', headers)
        yield b'501 Not Implemented'
    else:
        for key in dict:
            if path == '/'+key:
                start_response('200 OK', headers)
                yield dict[key].encode('ascii')
        else:
            start_response('404 Not Found', headers)
            yield b'404 not found'
    #start_response('200 OK', list(headers.items()))
    #yield 'Here is the WSGI environment:\r\n\r\n'.encode('utf-8')
    #yield pformat(environ).encode('utf-8')


if __name__ == "__main__":
    init()
    httpd = make_server('', 8000, app)
    host, port=httpd.socket.getsockname()
    print('Serving on', host, 'port', port)
    httpd.serve_forever()
