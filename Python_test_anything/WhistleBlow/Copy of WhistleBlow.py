# -*- coding: utf-8 -*-
import re
import time
import cx_Oracle
import urllib2
import os
import json
import md5

root = 'd:\\whistleblow\\'
start_time = time.clock()

file = open(root + 'lists\\urllist.txt', 'r')

i = 1
for line in file:
    print i
    try:
        res = urllib2.urlopen(line, timeout = 10)
    #print line
        page = open(root + 'pages2\\' + md5.md5(line).hexdigest(), 'w')
        page.write(res.read())
        page.close()
        res.close()
        time.sleep(1)
    except:
        print line
        pass

    
    i += 1   

