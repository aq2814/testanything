# -*- coding: utf-8 -*-
'''
Created on 2014. 11. 13.

@author: D2954_IPHONE5S
'''

file = open(u"D:\\엠엔형태소_테스트_141113.csv", 'r')
logfile = open(u"d:\\mn_dha_test_fin_141113.csv", 'w')

cnt = 0
for line in file:
    cnt += 1
    if cnt % 100000 == 0:
        print cnt
    fulllist = []
    list = []
    cate1 = ''
    cate2 = ''
    cate3 = ''
    cateid = ''
    list = line.split('","')
    fname = list[0].replace('"', '')
    #cate1 = list[1].replace('"', '')
    #cate2 = list[2].replace('"', '')
    #cate3 = list[3].replace('"', '')
    cateid = list[4].replace('"', '').replace('\n', '')
    #print list
    for a_part in fname.split('/'):
        
        txt = '"' + fname + '","' + a_part +  '","' + cateid + '"\n'
        #print txt    
        logfile.write(txt)
        #fname.decode('cp949') + '\t' + a_part.decode('cp949')
logfile.close()