#!/usr/bin/python3

from socket import *
import optparse
from threading import *

def comscan(thost,tport):
	try:
		sock=socket(AF_INET,SOCK_STREAM)
		sock.connect((thost,tport))
		print ("[+]%d/tcp is Open" % (tport))
	except:
		print ("[-]%d/tcp is close" % (tport))
	finally:
		sock.close()


def portscan(thost,tports):
	try:
		tip = gethostbyname(thost)
	except:
		print ("Unknow Host %s" %thost)
	try:
		tname = gethostbyaddr(tip)
		print("[*] Scan Result for :" + tname[0])
	except:
		print("[*] Scan Result for :" + tip)
	setdefaulttimeout(1)
	for tport in tports:
		t = Thread(target=comscan, args=(thost,int(tport)))
		t.start()
def main():
	parser = optparse.OptionParser("Usage " + " -H <target host>" + " -P <target port>")
	parser.add_option('-H', dest='thost', type='string', help='specify the target host')
	parser.add_option('-P', dest='tport', type='string', help='specify the target port')
	(options,args) = parser.parse_args()
	thost=options.thost
	tports=str(options.tport).split(',')
	if (thost == None) | (tports[0] == None):
		exit(0)
	portscan(thost,tports)

if __name__=='__main__':
	main()
