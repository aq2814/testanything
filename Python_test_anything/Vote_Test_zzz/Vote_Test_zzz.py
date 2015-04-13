'''
Created on 2014. 5. 27.

@author: D2954_IPHONE5S
'''
import urllib2

root = 'C:\\'

#http://sapi.map.daum.net/local/suji.fcgi?query=%EC%82%AC%EC%A0%84%ED%88%AC%ED%91%9C%EC%86%8C&page_size=100&page_no=1&service=poi_test&result_type=1

url_pre = 'http://sapi.map.daum.net/local/suji.fcgi?query=%EC%82%AC%EC%A0%84%ED%88%AC%ED%91%9C%EC%86%8C&page_size=1000&page_no='
#url_pre = 'http://sapi.map.daum.net/local/suji.fcgi?query=%ED%88%AC%ED%91%9C%EC%86%8C&page_size=1000&page_no='
url_post = '&service=poi_test&result_type=1'

file = open(root + 'vote_cid.txt', 'w')

for num in range(11):
    print url_pre + str(num + 1) + url_post
    open_url = urllib2.urlopen(url_pre + str(num + 1) + url_post)
    print open_url
    for ln in open_url:        
        if ln.replace(' ', '')[1:6] == 'docid':
            file.write(ln.replace(' ', '').replace('"docid":"', '').replace('",',''))

file.close()
    
    