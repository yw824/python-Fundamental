#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter03/tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, socket, random

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        print(more)
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                        ' %d bytes before the socket closed'
                        % (length, len(data)))
        data += more
    return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    attempt = 0
    sc, sockname = sock.accept()
    ans = random.randrange(1,11)
    print('We have accepted a connection from', sockname)
    while attempt < 5:
        print('Waiting to accept a new connection')
        message = recvall(sc, 2)
        input = message.decode()
        if int(input) == ans:
            message = b'Congratulations you did it'
            sc.sendall(message)
            break
        elif int(input) > ans:
            message = b'You guessed too high!     '
            sc.sendall(message)
        else:
            message = b'You guessed too small!    '
            sc.sendall(message)
        attempt += 1
    sc.close()
    print('  Reply sent, socket closed')

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    attempt = 0
    while attempt < 5:
        guess = input("input>> ")
        sock.sendall(guess.encode('ascii'))
        reply = recvall(sock, 26)
        if reply.decode() == 'Congratulations you did it':
            print(reply.decode())
            break
        else:
            print(reply.decode())
        attempt += 1
    sock.close()

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)