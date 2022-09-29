from pprint import pformat
from tracemalloc import start
from wsgiref.simple_server import make_server
import time

def app(environ, start_response):
    host = environ.get("HTTP_POST", '127.0.0.1')
    path = environ.get('PATH_INFO', '/')
    if ':' in host:
        host.port = host.split(":", 1)
    if '?' in path:
        path, query = path.split('?', 1)
    headers = [ ('Content-Type', 'text/plain; charset=utf-8') ]
    if environ['REQUEST_METHOD'] != 'GET':
        start_response('501 Not Implemented', headers)
        yield b'501 Not Implemented'
    elif path == '/foo':
        headers = headers + [('location', '/')]
        start_response('303 see other', headers)
        yield b'303 see other'
    elif host != '127.0.0.1' or path != '/':
        start_response('404 Not found', headers)
        yield b'404 Not found'
    else:
        start_response('200 Ok', headers)
        yield time.ctime().encode('ascii')

if __name__ == "__main__":
    httpd = make_server('', 8000, app)
    host, port=httpd.socket.getsockname()
    print('Serving on', host, 'port', port)
    httpd.serve_forever()

