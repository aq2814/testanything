'''
Created on 2014. 5. 15.

@author: D2954_IPHONE5S
'''
import cx_Oracle

cx = cx_Oracle.makedsn('10.12.225.12',1521,'spatialM')
connection = cx_Oracle.connect('place','place',cx)
cc1 = connection.cursor()
cc2 = connection.cursor()

stop_list = cc1.execute('select busstopid, busstopname, keywords from traffic.busstop_p')

cnt = 1

for a_row in stop_list:

    cnt += 1
    if cnt % 1000 == 0:
        connection.commit()
        print cnt

    pk = a_row[0]
    names1 = a_row[1].replace(',', '.').split('.')
    try:
        names2 = a_row[2].replace(',','|').split('|')
    except:
        names2 = ''
    
    for a_key1 in names1:
        #print str(pk) + '\t' + a_key1
        try:
            cc2.execute("INSERT INTO zzz_sh_busstop_p VALUES (:busstopid, :stopname)", {'busstopid':pk, 'stopname':a_key1})
        except:
            print str(pk) + '\t' + a_key1
    for a_key2 in names2:
        #print str(pk) + '\t' + a_key2
        cc2.execute("INSERT INTO zzz_sh_busstop_p VALUES (:busstopid, :stopname)", {'busstopid':pk, 'stopname':a_key2})  
    
connection.commit()
cc1.close()