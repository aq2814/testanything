# -*- coding: utf-8 -*-
import re
import time
import cx_Oracle
import urllib
import os
import json
import md5

root = 'd:\\whistleblow\\'
start_time = time.clock()

#appkey = '13e876069f3ca745dc54ac9a68450fb1'
appkey = '93e0a6820c8cbf9d36d74303aac2c838'

url1 = 'http://apihub.daum.net/search-news/v1/articles.json?q='
q = '%EB%82%B4%EB%B6%80%EA%B3%A0%EB%B0%9C' #내부고발
#q = '%EB%82%B4%EB%B6%80%EA%B3%A0%EB%B0%9C%EC%9E%90' #내부고발자
url2 = '&condition=title&page_no=' #내부고발자
url3 = '&page_size=10&appkey=' + appkey

idx = int(open(root + '0_idx.txt', 'r').read()) + 1

urllist = []
urlfile = open(root + '\\lists\\urllist.txt', 'r')
for a_url in urlfile:
    urllist.append(a_url.replace('\n', ''))
urlfile.close()

print urllist
os.chdir(root)
#os.mkdir(str(idx))
root2 = root + str(idx) + '\\'
j = 1

for i in range(5000):
    url = url1 + q + url2 + str(i + 1) + url3
    #url = url1 + q + url2 + '2' + url3
    print url
    res = urllib.urlopen(url)#, timeout = 10)
    json_res = res.read()
    print json_res
    res_cnt = json.loads(json_res)['channel']['result']
    page_cnt = int(json.loads(json_res)['channel']['totalCount']) / 10
    for cnt in range(int(res_cnt)):
        contents_url = json.loads(json_res)['channel']['item'][cnt]['contents_url']
        print contents_url
        
        try:
            if urllist.index(contents_url) >= 0:
                pass
        except:
            urllist.append(contents_url)
            urlfile = open(root + 'lists\\urllist.txt', 'a')
            urlfile.write(contents_url + '\n')
            urlfile.close()
            res2 = urllib.urlopen(contents_url)
            urlfilename = md5.md5(contents_url).hexdigest()
            urlpage = open(root + 'pages\\' + urlfilename, 'w')
            urlpage.write(res2.read())
            urlpage.close()
            pass
    """
    logfile = open(root2 + str(j) + '.txt', 'a')        
    logfile.write(res.read())
    logfile.close()"""

    time.sleep(1)
    j += 1
    if j > page_cnt:
        break

"""
    print 'except'
    open(root + '0_idx.txt', 'w').write(str(j))
    #logfile.close()

open(root + '0_idx.txt', 'w').write(str(j))
#logfile.close()
"""
urlfile.close()


    

