#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
C1 = '\033[1;36m'
G0 = '\033[0;32m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import requests,sys,os
from multiprocessing.pool import ThreadPool
def scan(site):
	try:
		if requests.get(site).status_code==200:
			print '%s[ %sLIVE %s] %s'%(W0,G0,W0,site)
			open('live_shell.txt','a+').write(site+'\n')
		else:
			print '%s[ %sDIEE %s] %s'%(W0,R0,W0,site)
	except:
		print '%s[ %sUNK %s] %s'%(W0,R0,W0,site)
		pass

try:
	os.system('clear')
	print '''%s
   _____ __  _______ __    __
  / ___// / / /__  // /   / /   %sCoded By ASTRO%s
  \__ \/ /_/ / /_ </ /   / /    %sTele: @ASTRO352%s
 ___/ / __  /___/ / /___/ /___  %sTele: @AnoneSecurity%s
/____/_/ /_//____/_____/_____/  CHECKER
'''%(C1,W0,C1,W0,C1,W0,C1)
	ThreadPool(30).map(scan,open(sys.argv[1]).read().splitlines())
	print '\n%s[ %sDONE %s] Saved in live_shell.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W0,R0,W0,W0))
except IndexError:
	exit('%s[%s!%s] Use : python2 %s target.txt \n%s[%s!%s] Fill in target.txt with http or https'%(W0,R0,W0,sys.argv[0],W0,R0,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W0,R0,W0,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W0,R0,W0,W0))
