'''
Created on 2014. 8. 12.

@author: D2954_IPHONE5S
'''

import os
import re
import cx_Oracle

connection = cx_Oracle.connect('place','placedb','PLACE')
cc1 = connection.cursor()

file = open('D:\\LGUPLUS\\11.txt', 'r')

i = 0
for line in file:
    line_attr = line.split('|')
    yearmonth = line_attr[0]
    phonenum = line_attr[1]
    dt = line_attr[2]
    val1 = line_attr[3]
    val2 = line_attr[4]
    val3 = line_attr[5]
    val4 = line_attr[6]
    val5 = line_attr[7]
    val6 = line_attr[8]
    val7 = line_attr[9]
    val8 = line_attr[10]
    val9 = line_attr[11]
    
    try:
        cc1.execute("INSERT INTO place.temp_cp_uplus_callhist \
        VALUES (:yearmonth, :phonenum, :lastcalldate, :totalcallcnt, :man10, :woman10, :man20, :woman20, :man30, :woman30, :man40, :woman40)",\
        {'yearmonth':yearmonth, 'phonenum':phonenum, 'lastcalldate':dt, 'totalcallcnt':val1, 'man10':val2, 'woman10':val3, 'man20':val4, 'woman20':val5, 'man30':val6, 'woman30':val7, 'man40':val8, 'woman40':val9})
    except:
        connection.commit()
        print 'error!'
        pass
    
    i += 1
    if i % 10000 == 0:
        print i
        connection.commit()
    
print i
connection.commit()
cc1.close()
