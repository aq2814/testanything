'''
Created on 2014. 5. 27.

@author: D2954_IPHONE5S
'''
import urllib2

root = 'C:\\'

#http://sapi.map.daum.net/local/suji.fcgi?query=%EC%82%AC%EC%A0%84%ED%88%AC%ED%91%9C%EC%86%8C&page_size=100&page_no=1&service=poi_test&result_type=1

url_pre1 = 'http://sapi.map.daum.net/local/suji.fcgi?query='
url_pre2 = '+%ED%88%AC%ED%91%9C%EC%86%8C&page_size=1000&page_no='
#url_pre = 'http://sapi.map.daum.net/local/suji.fcgi?query=%ED%88%AC%ED%91%9C%EC%86%8C&page_size=1000&page_no='
url_post = '&service=poi_test&result_type=1'

url_zone = ['%EC%84%9C%EC%9A%B8','%EA%B2%BD%EA%B8%B0','%EC%9D%B8%EC%B2%9C','%EA%B0%95%EC%9B%90','%EC%B6%A9%EB%B6%81','%EC%B6%A9%EB%82%A8','%EB%8C%80%EC%A0%84','%EA%B2%BD%EB%B6%81','%EA%B2%BD%EB%82%A8','%EB%8C%80%EA%B5%AC','%EB%B6%80%EC%82%B0','%EC%A0%84%EB%B6%81','%EC%A0%84%EB%82%A8','%EA%B4%91%EC%A3%BC','%EC%A0%9C%EC%A3%BC','%EC%84%B8%EC%A2%85','%EC%9A%B8%EC%82%B0']


file = open(root + 'vote_cid.txt', 'w')

for num in range(5):
    for zone in url_zone: 
        print url_pre1 + zone + url_pre2 + str(num + 1) + url_post
        open_url = urllib2.urlopen(url_pre1 + zone + url_pre2 + str(num + 1) + url_post)
        print open_url
        for ln in open_url:        
            if ln.replace(' ', '')[1:6] == 'docid':
                file.write(ln.replace(' ', '').replace('"docid":"', '').replace('",',''))

file.close()
    
    