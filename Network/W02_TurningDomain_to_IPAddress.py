# 2-1주차 강의교안 29페이지 내용에 해당

# gethostbyname() 메서드를 사용

import socket

if __name__ == "__main__":
    hostname = 'maps.google.com'
    addr = socket.gethostbyname(hostname)
    print("The IP Address of {} is {}".format(hostname, addr))

    hostname = "cse.ssu.ac.kr"
    addr = socket.gethostbyname(hostname)
    print("The IP Address of {} is {}".format(hostname, addr))