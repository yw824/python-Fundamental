from bz2 import compress
import json
import zlib
import socket
import ssl


class Solution():
    
    def special_bits(self, L=1, R=2, k=1):
        num = -2
        # Write your code between start and end for solution of problem 1
        # Start

        num = -1

        for i in range(L, R+1):
            count = 0
            stand = 1
            while stand <= i:
                if i & stand != 0:
                    count += 1
                stand *= 2

            if count == k:
                if num == -1:
                    num = i
                    break
        # End
        return num

    def toggle_string(self, S):

        # Write your code between start and end for solution of problem 2
        # Start
        s = ''

        for c in S:
            if(c.lower() == c):
                s += c.upper()
            elif (c.upper() == c):
                s += c.lower()
            else: # other case - non alphabet
                s += c

        # End
        return s

    def send_message(self, message):
        message = self.to_json(message)
        message = self.encode(message)
        message = self.compress(message)
        return message

    def recv_message(self, message):
        message = self.decompress(message)
        message = self.decode(message)
        message = self.to_python_object(message)
        return message
    
    # String to byte
    def encode(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        data = message.encode('utf-8')
        return data
        # End
        
    
    # Byte to string
    def decode(self,message):
        # Write your code between start and end for solution of problem 3
        # Start
        data = message.decode('utf-8')
        return data
        # End 

    # Convert from python object to json strin g
    def to_json(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        data = json.dumps(message)
        return data
        # End 

    # Convert from json string to python object
    def to_python_object(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        data = json.loads(message)
        return data
        # End 
    
    # Returns compressed message 
    def compress(self, message):
        # Write your code between start and end for solution of problem 3
        # Start
        data = zlib.compress(message)
        return data
        # End 

    # Returns decompressed message
    def decompress(self, compressed_message):
        # Write your code between start and end for solution of problem 3
        # Start
        data = zlib.decompress(compressed_message)
        return data
        # End 


    def client(self, host, port, cafile=None):
        # Write your code between start and end for solution of problem 4
        # Start
        cert = "" # Variable to store the certificate received from server 
        cipher = "" # Variable to store cipher used for connection
        msg = "" # Variable to store message received from server


        # End
        return cert, cipher, msg
    
    

    
