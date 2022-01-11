#!/usr/bin/python3
#[https://pexpect.readthedocs.io/en/stable/overview.html]
import pexpect

PROMPT = ['# ',  '>> ', '*:~# ', '\$ ']

def send_cmd(child,cmd):
	child.sendline(str(cmd))
	child.expect('root@localhost:~#')
	#child.expect([pexpect.TIMEOUT,'# ', '# ', '>> ', '*:~# ', '\$ '])

	print (child.before)
	print(child.after)

def connect(user,host,passwd):
	ssh_new = 'Are you sure you want to continue connecting (yes/no/[fingerprint])?'
	constr = 'ssh ' + user + '@' + host
	print (constr)
	child = pexpect.spawn(constr)
	ret = child.expect([pexpect.TIMEOUT,ssh_new,'[p|P]assword:'])
	if ret != 0:
		print ("[-] Error Connecting")
		#return
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT,"root@localhost's password:"])
		#if ret == 0:
		#	print ("[-] Erro Connecting")
			#return

	child.sendline(passwd)
	print (child.after)
	print (child.before)
	child.expect('root@localhost:~#')
	#child.expect([pexpect.TIMEOUT,'# ', '# ', '>> ', '*:~# ', '\$ '])
	#return child


def main():
	host = "localhost"
	user = "root"
	passwd = "54321"
	child = connect(user,host,passwd)
	if child is not None:
		send_cmd(child,'cat /etc/passwd')
	else:
		print("Problem connecting")
main()
