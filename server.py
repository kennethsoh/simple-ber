import asn1tools
import os
import sys
import socket
import json


def decode(data):
    test = asn1tools.compile_files('test.asn')
    decoded = test.decode('Data', data)
    return decoded

def ServerSocket():
    #create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Listen for incoming address
    server_address = ("192.168.56.9", 4444)
    sock.bind(server_address)
    print("waiting for incoming request from client")
    sock.listen(1)
    connection, client_address = sock.accept()
    with connection:
        print ("Connection received from", client_address)
        data = connection.recv(1024)
        decoded = decode(data)
        print("The decoded data is ", decoded)
        
    print("The value of the data is:", decoded.get("data"))


ServerSocket()

