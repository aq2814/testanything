'''
Created on 2015. 2. 3.

@author: D2954_IPHONE5S
'''

from itertools import *
from operator import itemgetter
import re
import time
import cx_Oracle

cx = cx_Oracle.makedsn('10.12.225.12',1521,'spatialM')
connection = cx_Oracle.connect('place','place',cx)
cc1 = connection.cursor()

start_time = time.clock()

p = re.compile(r'([1-9][0-9]{0,7}$)')
p2 = re.compile(r'(\d+$)')

file = open('c:\\Users\D2954_IPHONE5S\Desktop\New_Score\search_score_10.csv', 'r')

tdic = {}

cnt = 0

for obj in file:
    a_obj = obj.replace('\n', '').split(',')
    if len(a_obj) <> 5 or not p.match(a_obj[0]):
        continue
    cid = a_obj[0]
    
    #print cid, total_qcnt, total_ccnt, section_qcnt, section_ccnt
    
    if cid in tdic:
        for num in range(4):
            try:
                if p2.match(a_obj[num + 1]):
                    tdic[cid][num] = int(tdic[cid][num]) + int(a_obj[num + 1]) or 0
                else:
                    tdic[cid][num] = int(tdic[cid][num]) or 0
            except:
                pass
    else:
        tdic[cid] = [int(a_obj[1] or 0), int(a_obj[2] or 0), int(a_obj[3] or 0), int(a_obj[4] or 0)]
        pass

    cnt += 1
    if cnt % 1000000 == 0:
        print cnt
    
#print tdic

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))

start_time = time.clock()

M = []

cnt = 0
for a_num in range(len(tdic)):
    objs = tdic.popitem()
    M.append(tuple([int(objs[0])] + objs[1]))
    cnt += 1
    if cnt % 1000000 == 0:
        cc1.prepare("insert into zzz_sh_searchscore_test_10(confirmid, total_qcnt, total_ccnt, section_qcnt, section_ccnt) values (:1, :2, :3, :4, :5)")
        cc1.executemany(None, M)
        M = []
        connection.commit()

cc1.prepare("insert into zzz_sh_searchscore_test_10(confirmid, total_qcnt, total_ccnt, section_qcnt, section_ccnt) values (:1, :2, :3, :4, :5)")
cc1.executemany(None, M)
M = []
connection.commit()   
connection.close()
    
print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))

#file writing
"""
res_file = open('c:\\search_score_groupby.csv', 'w')
j = 0
res_file.write('cid,total_qcnt,total_ccnt,section_qcnt,section_ccnt\n')
for tkey in tdic:
    j += 1
    if j % 1000000 == 0:
        print j
    #print tkey
    
    tkey_obj = tdic[tkey]

    tf_1, tf_2, tf_3, tf_4 = str(tkey_obj[0]), str(tkey_obj[1]), str(tkey_obj[2]), str(tkey_obj[3])

    tf = tkey.split(',')
"""
    
"""
    if p2.match(tf_1):
        pass
    else:
        tf_1 = '0'
    if p2.match(tf_2):
        pass
    else:
        tf_2 = '0'
    if p2.match(tf_3):
        pass
    else:
        tf_3 = '0'
    if p2.match(tf_4):
        pass
    else:
        tf_4 = '0'"""
    
"""
    res_file.write(str(tkey) + ',' + tf_1 + ',' + tf_2 + ',' + tf_3 + ',' + tf_4 + '\n')

res_file.close()
print tdic
"""


"""
start_time = time.clock()

file = open('c:\\search_score.csv', 'r')

L = []

cnt = 0
ecnt = 0

p = re.compile(r'([1-9][0-9]{0,7}$)')
p2 = re.compile(r'(\d+$)')

for line in file:
    if cnt == 0:
        cnt += 1
        continue
    elif cnt % 1000000 == 0:
        print cnt
    try:
        line_list = line.replace('\n', '').split(',')
        
        if p.match(line_list[0]) > 0: 
            L.append(line_list)
            cnt += 1
        else:
            pass
            #print 'else', line
            ecnt += 1
    except:
        pass
        #print 'except', line
        ecnt += 1
    

print 'read complete'
print cnt, ecnt

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))

for key, group in groupby(sorted(L, key = itemgetter(0)), key = itemgetter(0)):
    print key, list(group)
    pass
"""