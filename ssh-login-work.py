#!/usr/bin/python3

import pexpect
#from termcolor import colored
PROMPT=['# ', '>>> ', '> ', '\$ ', '~# ']

def send_command(child,cmd):
	child.expect(PROMPT)
	child.sendline(cmd)
	print(child.before,child.after)



def connect(host,usr,passwd):
	ssh_key='Are you sure you want to continue connecting'
	conStr = 'ssh ' +usr+'@'+host
	child = pexpect.spawn(conStr)
	ret = child.expect([ssh_key,'[P|p]assword:'])
	if ret == 1:
		child.sendline('yes')
	if ret != 0:
		print ("Error connecting")
	child.sendline(passwd)
	child.expect(PROMPT)
	return child



def main():
	host = input(str("Enter the Target Host:"))
	usr = input(str("Enter the UserNmae:"))
	passwd = input(str("Enter the Password:"))
	child = connect(host,usr,passwd)
	send_command(child,'cat /etc/passwd')

main()


