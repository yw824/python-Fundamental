#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/client.py
# Simple Zen-of-Python client that asks three questions then disconnects.

import argparse, random, socket, zen_utils

def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    attempt = 0
    while attempt < 5:
        key = int(input("Input your Guess (1 to 10) >> "))
        sock.sendall((str(key)+'?').encode())
        attempt += 1
        _return = zen_utils.recv_until(sock, b'.')
        ans = _return.decode()
        ans = ans[0]
        ans = int(ans)
        if ans == 0:
            print("Congratulations you did it.")
            break
        elif ans == 1:
            print("You guessed too small!")
        elif ans == 2:
            print("You guessed too high!")
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    client(address)

# 실행 : python problem1_client.py -p 1060 127.0.0.1