#!/usr/bin/python3
import socket
from termcolor import colored
#creat socket
#ipv4,tcp
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host=str(input("[*] Enter the hostname or IP:"))

def scanner(port):
	if sock.connect_ex((host,port)):
		print(colored("[*] port %d is Closed" % (port),'red'))
	else:
		print(colored("[*]Port %d is Open" % (port),'green'))

for port in range(1,1000):
	scanner(port)

