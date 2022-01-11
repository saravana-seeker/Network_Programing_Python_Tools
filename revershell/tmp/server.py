#!/usr/bin/python3
import socket

#connect()

hostname='localhost'
port = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((hostname,port))
s.listen(5)

target,ip = s.accept()

print (str(target))
