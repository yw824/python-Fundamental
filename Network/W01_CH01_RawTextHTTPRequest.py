import socket # Internet Socket
import ssl # SSL( Secure Socket Layer ) for security
from urllib.parse import quote_plus # 문자열을 request 형식으로 바꾸는 작업을 수행

# Construct GET request ( GET operation followed by Headers )
request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: David\r\n\
Connection: Close\r\n\
\r\n\
"""

# r\ : carriage return( move cursor to the beginning )
# n\ : newline ( move to the next line )