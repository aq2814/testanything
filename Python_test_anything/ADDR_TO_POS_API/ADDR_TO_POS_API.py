# -*- coding: utf-8 -*-
import cx_Oracle
import mysql.connector
import urllib
import json
#from urllib import quote, unquote

cx = cx_Oracle.makedsn('10.12.225.12',1521,'spatialM')
connection = cx_Oracle.connect('place','place',cx)
cc1 = connection.cursor()

addrlist = cc1.execute('select pk, fulladdr from zzz_sh_auction7 where wpointx is null')

i = 1

pre = 'http://apis.daum.net/local/geo/addr2coord?apikey=360693ef2940083c86c65e2f8b8baa58440b129b&q='
post = '&output=json'

file = open('c:\\auction_temp.txt', 'w')

for ln in addrlist:
    pk = ln[0]
    addr = ln[1].decode('mbcs')
    url = pre + urllib.quote(unicode(addr).encode('utf8')) + post
    resp = urllib.urlopen(url)
    for ln2 in resp:
        #print ln2
        k = json.loads(ln2)
        cnt =  k['channel']['totalCount']
        #print cnt
        if cnt > 0:
            zzz = k['channel']['item']
            for a in zzz:
                res =  str(pk) + '\t' + a['point_wx'] + '\t' + a['point_wy'] + '\n'
                print res
                file.write(res)
            #print k['channel']['item']['point_wx']
    """
    i += 1
    if i == 5:
        break
    """
file.close()
connection.close()