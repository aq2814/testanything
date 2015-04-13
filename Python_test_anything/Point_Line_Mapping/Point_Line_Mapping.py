# -*- coding: utf-8 -*-
'''
Created on 2015. 2. 10.

@author: D2954_IPHONE5S
'''

#1) 모든 장소에 대해 XX미터 내 최근접 도로 4개를 찾는다
#2) 이렇게 다 찾은 후, 각 도로 별 장소 갯수를 group by 한다
#3) 도로 길이와 장소수를 잘 조합하면 도로의 인기도가 대략 나오지 않을까 싶다

#4) 모든 장소에 대해 XX미터 내 최근접 로드뷰 라인 1개를 찾는다
#5) 이렇게 다 찾은 후, 각 로드뷰 라인 별 갯수를 group by 한다...

#즉, 장소는, 도로와 로드뷰라인 두 개와의 SDO_NN 연산이 수행되어야 한다 


import cx_Oracle
import time

cx = cx_Oracle.makedsn('10.12.225.12',1521,'spatialM')
connection = cx_Oracle.connect('place','place',cx)
cco1 = connection.cursor()
cco2 = connection.cursor()

start_time = time.clock()

sql = "select confirmid from ndm.place_p where status = 'Y'"

resp = cco1.execute(sql)

map_list = []

sql_s = "select a.confirmid, b.objectid, sdo_nn_distance(1) as dist from \
ndm.place_p a, ndm.rdlink_l b \
where a.status = 'Y' and sdo_nn(b.shape, a.shape, 'sdo_num_res = 4, distance = 100', 1) = 'TRUE' \
and a.confirmid = "

cnt = 0

for a_cid in resp:
    map_list.append(cco2.execute(sql_s + str(a_cid[0])).fetchone())
    cnt += 1
    if cnt % 1000 == 0:
        print cnt
        print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))
    
print map_list

print ("Total " + "%f Seconds elasped!!" % (time.clock() - start_time))




"""

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
"""

connection.commit()   
connection.close()