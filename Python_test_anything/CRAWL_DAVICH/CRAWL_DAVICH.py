# -*- coding: utf-8 -*-
'''
Created on 2014. 11. 10.

@author: D2954_IPHONE5S
'''

import urllib2


def getDavich():
    url_pre =  'http://www.davich.com/04_market/01_find.php?pg='
    region = ['강원', '경기', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울', '울산광역시', '인천광역시', '전라남도', '전라북도', '제주', '충청남도', '충청북도']
    logfile = open('D:\\crawl\\davich\\logfile.txt', 'w')
    for a_region in region:
        for pagenum in range(100):
            #pagenum = 999
            url_full = url_pre + str(pagenum) + '&sido=' + a_region
            #print url_full
            resp = urllib2.urlopen(url_full, timeout = 10)
            chk1 = 0
            chk2 = 0
            chk3 = 0
            for a_line in resp:
                if a_line.find('pay_lest') > 0:
                    chk1 = 1
                elif a_line.find('div class="time"') > 0:
                    chk1 = 0
                
                if chk1 == 1:
                    if a_line.find('<tr>') > 0:
                        chk2 = 1
                        chk3 += 1
                        poi_info = ['','','']
                    elif a_line.find('</tr>') > 0:
                        chk2 = 0
                    if chk2 == 1:
                        #if a_line.find('width="282"') > 0:
                            #poi_info[0] = a_line[a_line.find('<strong>') + 8 : a_line.find('</strong>')]
                        if a_line.find('width="*') > 0:
                            poi_info[0] = a_line[a_line.find('<strong>') + 8 : a_line.find('</strong>')]
                        elif a_line.find('width="150"') > 0:
                            poi_info[1] = a_line[a_line.find('ter">') + 5 : a_line.find('</td>')].replace('-', '')
                        elif a_line.find('width="160"') > 0:
                            poi_info[2] = a_line[a_line.find('(') + 2 : a_line.find(')">') - 1].strip()                            
                            a_log = poi_info[0] + '\t' + poi_info[1] + '\t' + poi_info[2] + '\n'
                            logfile.write(a_log)
                            
                        #print a_line            
            
            if chk3 == 0:
                #print 'ZZZ'
                break           
        #logfile.close()
if __name__ == '__main__':
    getDavich()