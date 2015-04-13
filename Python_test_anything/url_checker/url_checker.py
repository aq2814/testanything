# -*- coding: utf-8 -*-
import re
import time
import cx_Oracle
import urllib2

cx = cx_Oracle.makedsn('10.12.225.12',1521,'spatialM')
connection = cx_Oracle.connect('place','place',cx)
cc0 = connection.cursor()
cc1 = connection.cursor()
cc2 = connection.cursor()

root = 'd:\\py_study'
start_time = time.clock()

cc0.execute('truncate table zzz_sh_urlerror_res')

def url_format_checker(input_url):   
    if input_url[0][:7] <> 'http://' and input_url[0][:7] <> 'https:/':
        checked_url = 'http://' + input_url[0]
    else:
        checked_url = input_url[0]
    return checked_url
    #unicode

def fetch_to_list(input_fetch):
    #i = 1
    a_list = []
    for a_entity in input_fetch:
        a_entity = url_format_checker(a_entity)
        a_list.append(a_entity)
        """
        i += 1
        if i == 1000:
            break"""
    return a_list
        
def url_res_checker(input_url):
    try:
        resp = urllib2.urlopen(input_url, timeout = 10)
        resp_list = [input_url, resp.geturl(), resp.getcode(), len(resp.read())]
    except:
        resp_list = [input_url, '', 'err', '0']
    return resp_list

def main():
    #cc1.execute("truncate table zzz_sh_urlerror_res")
    url_all = cc2.execute("select distinct homepage from zzz_sh_urlerror_org")
    print "DB connection success"
    
    url_list = fetch_to_list(url_all)
    
    print "Getting url is done"
    
    j = 1
    
    for a_url in url_list:
        res = url_res_checker(a_url)
        cc1.execute("INSERT INTO place.zzz_sh_urlerror_res VALUES (:url_org, :url_red, :url_code, :url_size)", \
                    {'url_org':res[0], 'url_red':res[1], 'url_code':res[2], 'url_size':res[3]})
        #print res
        connection.commit()
        print res
        
    j += 1

if __name__ == '__main__':
    main()
    
cc1.close()
cc2.close()

"""


    confirmid = url_s[0]
    url = unicode(url_s[1])
    print url

    try:
        resp = urllib2.urlopen(url)
        print 'Good'
    except:
        cc2.execute("insert into place.zzz_sh_urlerror_res values (:confirmid, :homepage)",\
                    {'confirmid':confirmid, 'homepage':url}\
                    )
        cnt = cnt + 1
        connection.commit()

print 'Total ' + str(cnt) + ' / ' + str(j) + ' bad urls are founded!'
print ("Total " + "%d Seconds elasped!!" % (time.clock() - start_time))

connection.commit()



"""
"""
cc1.execute("INSERT INTO place.zzz_sh_cr_nd_dupl VALUES (:seq, :confirmid, :sid, :qver, :distance, :eq_phone, :type,\
        :decision_score, :total_score, :score_name, :score_fullname, :score_addr, :score_dist, :score_nd, :score_fnd, :score_w,\
        :score_fw)", {'seq':seq, 'confirmid':confirmid, 'sid':sid, 'qver':qver, 'distance':distance, 'eq_phone':eq_phone,\
                      'type':type, 'decision_score':decision_score, 'total_score':total_score, 'score_name':score_name,\
                      'score_fullname':score_fullname, 'score_addr':score_addr, 'score_dist':score_dist, 'score_nd':score_nd, 'score_fnd':score_fnd, 'score_w':score_w, 'score_fw':score_fw})
                      """