#!/usr/bin/python3

import socket

#creating a socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)


hostname=str(input("Please Enter the IP:"))
port=int(input("Please Enter The Port:"))

#for x in port:
#	print(port)

def portscanner(port):
	if sock.connect_ex((hostname,port)):
		print("Port %d is closed" % (port))
	else:
		print("Port %d is Open" % (port))

portscanner(port)



#if sock.connect_ex((host,port)) its makea a error 



