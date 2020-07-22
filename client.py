import asn1tools
import socket
import argparse


ipaddr = input("Enter Server's ip address: ")
data = str(input("Enter data to encode and send: "))

def encode(data):
    test = asn1tools.compile_files('test.asn')
    encoded = test.encode('Data',{'id':1, 'ipaddr': ipaddr, 'data':data})
    print("Encoded value is ", encoded)
    return encoded

def ClientSocket(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ipaddr, 4444)
    sock.connect(server_address)
    encoded = encode(data)
    sock.send(encoded)

ClientSocket(data)
