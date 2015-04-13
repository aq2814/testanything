'''
Created on 2014. 5. 15.

@author: D2954_IPHONE5S
'''
import cx_Oracle

cx = cx_Oracle.makedsn('10.12.225.12',1521,'spatialM')
connection = cx_Oracle.connect('place','place',cx)
cc1 = connection.cursor()
cc2 = connection.cursor()

stop_list = cc1.execute("select cateid, synonym3 from zzz_sh_cate where synonym3 is not null and id1 not in (3439, 18435)")

cnt = 1

for a_row in stop_list:

    cnt += 1
    if cnt % 1000 == 0:
        connection.commit()
        print cnt

    pk = a_row[0]
    names1 = a_row[1].split(';')
    
    for a_key1 in names1:
        #print str(pk) + '\t' + a_key1
        
        cc2.execute("INSERT INTO zzz_sh_cate2 VALUES (:cateid, :syn)", {'cateid':pk, 'syn':a_key1})  
    
connection.commit()
cc1.close()