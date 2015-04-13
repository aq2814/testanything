# -*- coding: utf-8 -*-

import urllib
import json
import math

#url1 = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/areaCode?ServiceKey=7mhWn2vEf%2FkCnDcdI4K0aFLu2VEKXm%2B4Qf0Aj8a0wf6ACoGbzWnDRQci0w9r6MBO28Eksev6l4cX9MUjS6iM7w%3D%3D&areaCopde=1&numOfRows=10&pageNo=1&_type=json'
url1 = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/areaBasedList?'
#url1 = 'http://api.visitkorea.or.kr/openapi/service/rest/EngService/areaCode?'
url2 = 'ServiceKey=7mhWn2vEf%2FkCnDcdI4K0aFLu2VEKXm%2B4Qf0Aj8a0wf6ACoGbzWnDRQci0w9r6MBO28Eksev6l4cX9MUjS6iM7w%3D%3D&'
url3 = 'areaCode='
url4 = '&numOfRows='
url5 = '&pageNo='
url6 = '&MobileOS=ETC&MobileApp=AppTesting&_type=json'

fullurl = url1 + url2 + url3
areacode = ['1', '2', '3', '4', '5', '6', '7', '8', '31', '32', '33', '34', '35', '36', '37', '38']
numofrows = 1000

logfile = open('C:\\tourpoi.txt', 'w')
header = 'addr1\taddr2\tareacode\tcat1\tcat2\tcat3\tcontentid\tcontenttypeid\tcreatedtime\tfirstimage\tfirstimage2\tmapx\tmapy\tmlevel\tmodifiedtime\treadcount\tsigungucode\ttel\ttitle\n'
logfile.write(header)

for area in areacode:
    url = url1 + url2 + url3 + area + url4 + str(numofrows) + url5 + '1' + url6
    print url
    resp = urllib.urlopen(url)
    a = json.load(resp)
    cnt = a['response']['body']['totalCount']
    print 'areacode: ' + area + '\t' + 'cnt: ' + str(cnt)
    pagecnt = int(math.ceil(cnt / float(numofrows)))
    for pagenum in range(pagecnt):        
        url_new = url1 + url2 + url3 + area + url4 + str(numofrows) + url5 + str(pagenum + 1) + url6
        print url_new
        resp2 = urllib.urlopen(url_new)
        b = json.load(resp2)
        
        if cnt >= numofrows:
            cnt = cnt - numofrows
            cnt2 = numofrows
        else:
            cnt2 = cnt
        
        for rnum in range(cnt2 - 1):
            content_all = a['response']['body']['items']['item'][rnum]
    
            addr1 = ''
            addr2 = ''
            areacode = ''
            cat1 = ''
            cat2 = ''
            cat3 = ''
            contentid = ''
            contenttypeid = ''
            createdtime = ''
            firstimage = ''
            firstimage2 = ''
            mapx = ''
            mapy = ''
            mlevel = ''
            modifiedtime = ''
            readcount = ''
            sigungucode = ''
            tel = ''
            title = ''
            
            try:
                addr1 = content_all['addr1']
            except:
                pass
            try:
                addr2 = content_all['addr2']
            except:
                pass
            try:
                areacode = content_all['areacode']
            except:
                pass
            try:
                cat1 = content_all['cat1']
            except:
                pass
            try:
                cat2 = content_all['cat2']
            except:
                pass
            try:
                cat3 = content_all['cat3']
            except:
                pass
            try:
                contentid = content_all['contentid']
            except:
                pass
            try:
                contenttypeid = content_all['contenttypeid']
            except:
                pass
            try:
                createdtime = content_all['createdtime']
            except:
                pass
            try:
                firstimage = content_all['firstimage']
            except:
                pass
            try:
                firstimage2 = content_all['firstimage2']
            except:
                pass
            try:
                mapx = content_all['mapx']
                mapy = content_all['mapy']
            except:
                pass
            try:
                mlevel = content_all['mlevel']
            except:
                pass
            try:
                modifiedtime = content_all['modifiedtime']
            except:
                pass
            try:
                readcount = content_all['readcount']
            except:
                pass
            try:
                sigungucode = content_all['sigungucode']
            except:
                pass
            try:
                tel = content_all['tel']
            except:
                pass
            try:
                title = content_all['title']
            except:
                pass
            
            text1 = addr1 + '\t' + str(addr2) + '\t' + str(areacode) + '\t' + cat1 + '\t' + cat2 + '\t' + cat3 + '\t' + str(contentid) + '\t' + str(contenttypeid) + '\t' + str(createdtime)
            text2 = firstimage + '\t' + firstimage2 + '\t' + str(mapx) + '\t' + str(mapy) + '\t' + str(mlevel) + '\t' + str(modifiedtime) + '\t' + str(readcount) + '\t' + str(sigungucode) + '\t' + tel + '\t' + title + '\n'
            fulltext = text1 + text2   
              
            logfile.write(fulltext) 
            
logfile.close()
