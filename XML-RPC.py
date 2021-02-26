#!/usr/bin/python
#/* Coded By ASTRO */#
#/* Kurd-H.org     */#

import requests
import os
import sys
import re
from urlparse import urlparse
from os import system, name
from time import sleep
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from ConfigParser import ConfigParser
from Queue import Queue
from colorama import Fore
from colorama import Style
from colorama import init
import random
init(autoreset=True)
try:
    os.mkdir('Checked')
except:
    pass
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
class Worker(Thread):

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                print e

            self.tasks.task_done()


class ThreadPool:

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()


def printf(text):
    ''.join([ str(item) for item in text ])
    print text + '\n',


def main(url):
    try:
        text = ' \x1b[1;30;40mSite:\x1b[0m ' + url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0'
           }
        get_jembut = requests.get(url + '/xmlrpc.php', headers=headers, timeout=2).content
        if 'XML-RPC server accepts POST requests only.' in get_jembut:
            text += ' | \x1b[32;1m YES\x1b[0m'
            open('Checked/results.txt', 'a').write(url + '\n')
        else:
            text += ' | \x1b[31;1mNO\x1b[0m'
    except:
        text = ' \x1b[1;30;40mSite:\x1b[0m ' + url
        text += ' | \x1b[31;1mNO\x1b[0m'

    printf(text)
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
ee = random.choice([r,g,y,b,m,c,w])

if __name__ == '__main__':
    print ee+"\n _                 _______  ______                  \n| \    /\|\     /|(  ____ )(  __  \        |\     /|\n|  \  / /| )   ( || (    )|| (  \  )       | )   ( |\n|  (_/ / | |   | || (____)|| |   ) | _____ | (___) |\n|   _ (  | |   | ||     __)| |   | |(_____)|  ___  |\n|  ( \ \ | |   | || (\ (   | |   ) |       | (   ) |\n|  /  \ \| (___) || ) \ \__| (__/  )       | )   ( |\n|_/    \/(_______)|/   \__/(______/        |/     \|\n"
    try:
        lists = sys.argv[1]
        numthread = sys.argv[2]
        readsplit = open(lists).read().splitlines()
    except:
        try:
            lists = raw_input(' \x1b[91mKurd-H@ASTRO [List] :~# \x1b[95m \x1b[90m')
            readsplit = open(lists).read().splitlines()
        except:
            print ' \x1b[91m[-] \x1b[90mKurd-H@ASTRO:~# \x1b[95m cat error_lists.txt\x1b[90m'
            print ' \x1b[1;31;40mError Enter Site List!'
            exit()

        try:
            numthread = raw_input(' \x1b[91mKurd-H@ASTRO [Threads] :~#\x1b[95m \x1b[90m')
        except:
            print ' \x1b[91m[-] \x1b[90mKurd-H@ASTRO:~#\x1b[95m cat error_threads.txt\x1b[90m'
            print ' \x1b[1;31;40mError Enter Threads!'
            exit()

    pool = ThreadPool(int(numthread))
    for url in readsplit:
        if '://' in url:
            url = url
        else:
            url = 'http://' + url
        if url.endswith('/'):
            url = url[:-1]
        jagases = url
        try:
            pool.add_task(main, url)
        except KeyboardInterrupt:
            exit()

    pool.wait_completion()
content = open('Checked/results.txt', 'r').readlines()
content_set = set(content)
print ' Cleaning Result Was Successful'
cleandata = open('Checked/results_clean.txt', 'w')
for line in content_set:
    cleandata.write(line)

os.remove('Checked/results.txt')
