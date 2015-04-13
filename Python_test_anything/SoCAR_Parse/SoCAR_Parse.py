# -*- coding: utf-8 -*-

'''
Created on 2014. 11. 28.

@author: D2954_IPHONE5S
'''

import urllib
import json
import cx_Oracle

def main():
    connection = cx_Oracle.connect('place','placedb','PLACE')
    cc1 = connection.cursor()
    cc2 = connection.cursor()
    cc3 = connection.cursor()
    
    url = 'http://api.socar.kr/daumpoi?code=B34B85840A31BAA944BAD7414EED8E33'
    
    #file = open('c:\\socar.csv', 'w')
    
    cc1.execute('truncate table temp_cp_socar')
    cc1.close()
    
    resp = urllib.urlopen(url)
    
    a = json.load(resp)
    
    cnt =  a['body']['totalcount']
    
    for a_row in range(cnt):
        
        id = ''
        name = ''
        sido = ''
        gugun = ''
        dong = ''
        address = ''
        open = ''
        close = ''
        latitude = ''
        longitude = ''
        
        item = a['body']['item'][a_row]
        id = item['id'].strip()
        name = item['name'].strip()
        sido = item['sido'].strip()
        gugun = item['gugun'].strip()
        dong = item['dong'].strip()
        address = item['address'].replace('\t', '').strip()
        open = item['open'].strip()
        close = item['close'].strip()
        latitude = item['latitude'].strip()
        longitude = item['longitude'].strip()
        
        cc2.execute("INSERT INTO temp_cp_socar VALUES (:placeid, :placename, :sido, :gugun, :dong, :address, :open, :close, :latitude, :longitude)", \
        {'placeid':id, 'placename':name, 'sido':sido, 'gugun':gugun, 'dong':dong, 'address':address, 'open':open, 'close':close, 'latitude':latitude, 'longitude':longitude})
        connection.commit()
    cc2.close()

    out_rescode = ''
    out_sqlmsg = ''

    cc3.callproc("PROC_TEMP_TO_CP_SOCAR", [out_rescode, out_sqlmsg])
    cc3.close()
    connection.close()

if __name__ == '__main__':
    main()