# -*- coding: utf-8 -*-

'''
Created on 2014. 11. 6.

@author: D2954_IPHONE5S
'''
import mysql.connector

#conn = mysql.connector.connect(user='cms', password='vlrtmTldpadptm!@#$',host='114.108.155.21', database='pvc')
conn = mysql.connector.connect(user='cms', password='vlrtmTldpadptm!@#$',host='114.108.155.50', database='taxi')
cc = conn.cursor()

tdic = {}

file = open(u'C:\\TaxiMach_Link_Dataset_Compact_201411_v141210.txt')
i = 0
for ln in file:
    i += 1
    try:
        tlist = ln.split(',')
        linkid = tlist[0]
        day = tlist[1]
        time = tlist[2]
        pk = str(linkid) + ',' + str(day) + ',' + str(time)
        
        cnt_all = int(tlist[5]) + int(tlist[6])
        if pk in tdic:
            tdic[pk] = tdic[pk] + cnt_all
        else:
            tdic[pk] = cnt_all        
            
    except:
        print 'exception!!'
        pass

    if i % 1000000 == 0:
        print i
        #break

print 'parsing finished!!!'
 
j = 0

res_file = open('d:\\zzz.csv', 'w')

for tkey in tdic:
    j += 1
    if j % 10000 == 0:
        print j
    #print tkey
    
    cnt_val = tdic[tkey]
    """
    qr = "insert into taxi.taxi_cellcd_cnt values (%s, %s)"
    vl = (tkey, cnt_val)
    cc.execute(qr, vl)
    if j % 10000 == 0:
        print j
        conn.commit()
    j += 1"""
    tf = tkey.split(',')
    res_file.write(tf[0] + ',' + tf[1] + ',' + tf[2] + ',' + str(cnt_val) + '\n')

res_file.close()
cc.close()
print j
    