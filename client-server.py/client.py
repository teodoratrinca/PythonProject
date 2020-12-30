import socket
import requests
import sys
import pickle

host = '127.0.0.1'
port = 2727

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
        msg = s.recv(4096)
        print(msg.decode("utf-8"))
        movie = input("Filmul despre care doresc sa aflu mai multe informatii: ")
        s.sendall(str.encode(movie))
        msg = s.recv(4096)  # primesc ratingul despre filmul pe care il doresc
        recd = pickle.loads(msg)
        print(recd)
        #print(type(recd))




